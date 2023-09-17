import logging
from transformers import AutoModelForCausalLM
import transformers


class AI:
    def __init__(self, model_path):
        self.model_path = model_path
        self.started = False

    def initialize(self):
        config = transformers.AutoConfig.from_pretrained(
            self.model_path, rope_scaling={}  # llama 2 specific? optimization setting
        )
        # TODO add some more optins, 4 bits quantizations, etc...
        self.model = AutoModelForCausalLM.from_config(config)
        self.tokenizer = transformers.AutoTokenizer.from_pretrained(self.model_path)

    def feed_input(self, prompt: str, system_prompt: str = ""):
        if not self.started:
            logging.critical("AI have not been started yet")
            return
        # https://huggingface.co/docs/transformers/v4.33.0/en/llm_tutorial#common-pitfalls
        # TODO add token streaming
        input = self.tokenizer(system_prompt + prompt, return_tensors="pt").to("cuda")
        generated_ids = self.model.generate(**input)
        output = self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
        return output
