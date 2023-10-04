from os import PathLike
from typing import Any
import logging
import torch
from transformers import AutoModelForCausalLM, AutoConfig, AutoTokenizer

_started = False
_model: Any = None
_tokenizer: Any = None


def start(model_path: PathLike | str):
    global _model, _tokenizer, _started

    if _started:
        logging.warn("Stop the currently running AI before starting a new one.")
        return

    config = AutoConfig.from_pretrained(
        model_path, rope_scaling={}  # llama 2 specific? optimization setting
    )
    # TODO add some more optins, 4 bits quantizations, etc...
    _model = AutoModelForCausalLM.from_pretrained(
        model_path, config=config, local_files_only=True
    )
    _tokenizer = AutoTokenizer.from_pretrained(model_path)
    _started = True


def stop():
    global _model, _tokenizer, _started

    _started = False
    del _model
    del _tokenizer
    torch.cuda.empty_cache()


# TODO add async
def feed_input(prompt: str, system_prompt: str = "") -> str:
    global _model, _tokenizer, _started

    if not _started:
        logging.warn("AI have not been started yet")
        return ""
    # https://huggingface.co/docs/transformers/v4.33.0/en/llm_tutorial#common-pitfalls
    # TODO add token streaming
    input = _tokenizer(system_prompt + prompt, return_tensors="pt").to("cuda")
    generated_ids = _model.generate(**input)
    output = _tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
    return output[0]
