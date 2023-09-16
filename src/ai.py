from transformers import AutoModelForCausalLM
import transformers

class AI():
    def __init__(self):
        model_path = "/model"
        
        config = transformers.AutoConfig.from_pretrained(
            model_path,
            rope_scaling={} # llama 2 specific? optimization setting
        )
        
        # TODO add some more optins, 4 bits quantizations, etc...
        model = AutoModelForCasualLM.from_config(config)
        tokenizer = transformers.AutoTokenizer.from_pretrained(model_path)


    def feed_input(prompt: str):
        # https://huggingface.co/docs/transformers/v4.33.0/en/llm_tutorial#common-pitfalls
        input = tokenizer(SYSTEM_PROMPT + PROMPT, return_tensors="pt").to("cuda")
        generated_ids = model.generate(**input)
        output = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
        return ouput
