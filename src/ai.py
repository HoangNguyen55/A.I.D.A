from transformers import AutoModelForCasualLM
import transformers

SYSTEM_PROMPT = ""
PROMPT = ""

model_path = "/model"

config = transformers.AutoConfig.from_pretrained(
    model_path,
    rope_scaling={}
)

model = AutoModelForCasualLM.from_config(config)
tokenizer = transformers.AutoTokenizer.from_pretrained(model_path)

# https://huggingface.co/docs/transformers/v4.33.0/en/llm_tutorial#common-pitfalls
input = tokenizer(SYSTEM_PROMPT + PROMPT, return_tensors="pt").to("cuda")
generated_ids = model.generate(**input)
output = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
