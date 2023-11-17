from os import PathLike
from typing import Any
import logging
import torch
import time
from threading import Thread
from queue import Queue
from transformers import (
    AutoModelForCausalLM,
    AutoConfig,
    AutoTokenizer,
    BitsAndBytesConfig,
    TextIteratorStreamer,
)


class _AI:
    def __init__(self) -> None:
        self._started = False
        self._model: Any = None
        self._tokenizer: Any = None
        self._inference_thread: Thread
        self._input_queue: Queue[tuple[int, str]] = Queue(5)
        self._output_dict: dict[int, TextIteratorStreamer] = {}

    def start(self, model_path: PathLike | str):
        logging.info(f"Starting the AI at '{model_path}'")
        if self._started:
            logging.warn("Stop the currently running AI before starting a new one.")
            return

        quantize_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_use_double_quant=True,
            bnb_4bit_compute_dtype=torch.bfloat16,
        )

        config = AutoConfig.from_pretrained(
            model_path,
            # torch_dtype=torch.bfloat16, # use bfloat 16 when training
            rope_scaling={
                "type": "dynamic",
                "factor": 2.0,
            },
            local_files_only=True,
        )
        self._model = AutoModelForCausalLM.from_pretrained(
            model_path,
            config=config,
            quantization_config=quantize_config,
            local_files_only=True,
            device_map="auto",
        )
        self._tokenizer = AutoTokenizer.from_pretrained(model_path)
        self._started = True
        self._inference_thread = Thread(target=self._inference_loop, daemon=True)
        self._inference_thread.start()

    def stop(self):
        self._started = False
        self._inference_thread.join()
        del self._model
        del self._tokenizer
        torch.cuda.empty_cache()

    def _inference_loop(self):
        # this loop is to be run in another thread
        while self._started:
            return_id, user_input = self._input_queue.get()
            prompt = f"""
            <s>[INST] <<SYS>>
            You are a nice assistant that will answer questions correctly
            <</SYS>>
            
            {user_input} [/INST]
            """

            input = self._tokenizer(prompt, return_tensors="pt").to("cuda:0")
            streamer = TextIteratorStreamer(self._tokenizer, skip_prompt=True)
            decode_kwargs = dict(input, streamer=streamer)
            thread = Thread(
                target=self._model.generate, kwargs=decode_kwargs, daemon=True
            )
            thread.start()
            self._output_dict[return_id] = streamer
            # thread.join()

    def feed_input(
        self, prompt: str, system_prompt: str = ""
    ) -> TextIteratorStreamer | str:
        if not self._started:
            logging.warn("AI have not been started yet")
            return "AI have not been started yet"
        # https://huggingface.co/docs/transformers/v4.33.0/en/llm_tutorial#common-pitfalls
        if self._input_queue.full():
            return "Maxium input queue exceeded (5)"

        complete_prompt = prompt + system_prompt
        return_id = int(time.time())
        self._input_queue.put((return_id, complete_prompt), block=False)

        streamer = self._output_dict.pop(return_id, None)
        while streamer == None:
            streamer = self._output_dict.pop(return_id, None)

        return streamer


AI = _AI()
