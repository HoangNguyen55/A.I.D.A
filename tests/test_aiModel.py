from huggingface_hub import login
token = "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"
login(token)

from datasets import load_dataset
import torch
from transformers import AutoModelForCausalLM, BitsAndBytesConfig, AutoTokenizer, TrainingArguments
from peft import LoraConfig
from trl import SFTTrainer
import transformers
from transformers import LlamaModel, LlamaConfig

configuration = LlamaConfig()


model = LlamaModel(configuration)
configuration = model.config

tokenizer = AutoTokenizer.from_pretrained("/home/xbl5229/llama/llama-2-7b-chat")
pipeline = transformers.pipeline(
    "text-generation",
    model="/home/xbl5229/llama/llama-2-7b-chat",
    torch_dtype=torch.float16,
    device_map="auto", )

input = 'I liked "Breaking Bad" and "Band of Brothers". Do you have any recommendations of other shows I might like?\n'
def IPnOP (input: str)-> None:
    sequences = pipeline(
        input,
        do_sample=True,
        top_k=10,
        num_return_sequences=1,
        eos_token_id=tokenizer.eos_token_id,
        max_length=200,
    )

    for seq in sequences:
        print(f"Result: {seq['generated_text']}")

print(IPnOP(input))

