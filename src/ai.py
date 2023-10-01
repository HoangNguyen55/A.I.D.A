import logging
import torch
from transformers import AutoModelForCausalLM, AutoConfig, AutoTokenizer


class AI:
    def __init__(self, model_path):
        self._model_path = model_path
        self._started = False
        self._model
        self._tokenizer

    def start(self):
        config = AutoConfig.from_pretrained(
            self._model_path, rope_scaling={}  # llama 2 specific? optimization setting
        )
        # TODO add some more optins, 4 bits quantizations, etc...
        self._model = AutoModelForCausalLM.from_pretrained(
            self._model_path, config=config, local_files_only=True
        )
        self._tokenizer = AutoTokenizer.from_pretrained(self._model_path)
        self._started = True

    def stop(self):
        self._started = False
        del self._model
        del self._tokenizer
        torch.cuda.empty_cache()

    # TODO add async
    def feed_input(self, prompt: str, system_prompt: str = "") -> str:
        if not self._started:
            logging.warn("AI have not been started yet")
            return ""
        # https://huggingface.co/docs/transformers/v4.33.0/en/llm_tutorial#common-pitfalls
        # TODO add token streaming
        input = self._tokenizer(system_prompt + prompt, return_tensors="pt").to("cuda")
        generated_ids = self._model.generate(**input)
        output = self._tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
        return output[0]
