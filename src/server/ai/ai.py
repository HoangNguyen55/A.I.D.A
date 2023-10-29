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
        if self.started:
            logging.warn("Stop the currently running AI before starting a new one.")
            return

        config = AutoConfig.from_pretrained(
            model_path, rope_scaling={}  # llama 2 specific? optimization setting
        )
        # TODO add some more optins, 4 bits quantizations, etc...
        self.model = AutoModelForCausalLM.from_pretrained(
            model_path, config=config, local_files_only=True
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
            return ""
        # https://huggingface.co/docs/transformers/v4.33.0/en/llm_tutorial#common-pitfalls
        # TODO add token streaming
        input = self.tokenizer(system_prompt + prompt, return_tensors="pt").to("cuda")
        generated_ids = self.model.generate(**input)
        output = self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
        return output[0]


AI = _AI()
