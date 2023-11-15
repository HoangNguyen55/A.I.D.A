from os import PathLike
from typing import Any
import logging
import torch
from transformers import AutoModelForCausalLM, AutoConfig, AutoTokenizer


class _AI:
    def __init__(self) -> None:
        self.started = False
        self.model: Any = None
        self.tokenizer: Any = None

    def start(self, model_path: PathLike | str):
        logging.info(f"Starting the AI at '{model_path}'")
        if self.started:
            logging.warn("Stop the currently running AI before starting a new one.")
            return

        config = AutoConfig.from_pretrained(
            model_path,
            # torch_dtype=torch.bfloat16, # use bfloat 16 when training
            rope_scaling={
                "type": "dynamic",
                "factor": 2.0,
            },
            local_files_only=True,
        )
        # TODO add some more optins, 4 bits quantizations, etc...
        self.model = AutoModelForCausalLM.from_pretrained(
            model_path,
            config=config,
            local_files_only=True,
            device_map="auto",
            load_in_4bit=True,
        )
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.started = True

    def stop(self):
        self.started = False
        del self.model
        del self.tokenizer
        torch.cuda.empty_cache()

    # TODO add async
    def feed_input(self, prompt: str, system_prompt: str = "") -> str:
        if not self.started:
            logging.warn("AI have not been started yet")
            return "AI have not been started yet"
        # https://huggingface.co/docs/transformers/v4.33.0/en/llm_tutorial#common-pitfalls
        # TODO add token streaming
        input = self.tokenizer(system_prompt + prompt, return_tensors="pt").to("cuda:0")
        logging.debug(input)
        generated_ids = self.model.generate(**input)
        output = self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
        return " ".join(output)


AI = _AI()
