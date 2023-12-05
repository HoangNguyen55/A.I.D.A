from random import randint
from transformers import AutoModelForCausalLM
from transformers import AutoTokenizer
import time
from transformers import LlamaTokenizer
from transformers import LlamaForCausalLM
from transformers import AutoConfig,TextStreamer
from langdetect import detect, detect_langs

while True:
  
    prompt = "Enter Prompt:  "
    user_prompt = input(prompt)
    texts = [user_prompt]
    # prompt = ""
    # <s>[INST] <<SYS>>
    # {{ system_prompt }}
    # <</SYS>>

    # {{ user_message }} [/INST]
    # https://www.philschmid.de/llama-2#how-to-prompt-llama-2-chat 



    def langdetect(text):
        languages = []
        for text in texts:
            languages.append((detect_langs(text)))
        return languages
    ens = False
    try:
        x = langdetect(user_prompt)
        if 'en' in str(x[0][0]):
            ens= True
    except:
        ens= True

    repoid= '/slrmstore/xbl5229/Finetuned_Model'


    model = AutoModelForCausalLM.from_pretrained(
        repoid, device_map="auto", load_in_4bit=True)

    token = AutoTokenizer.from_pretrained(repoid,padding_side="left")



    if ens==False :
        sys_prompt = "You are a nice assistant, answer questions as polite as possible and be correct"
    else:
        if randint(1,2)==2:
            sys_prompt = "You are a nice assistant, answer questions as polite as possible and be correct"
        else:
            sys_prompt = "You are an assistant, answer questions as condescending, passive-aggressive and mean as possible, but make sure to give correct informations."

        


    complete_prompt = f"""
            <s>[INST] <<SYS>>
            {sys_prompt}
            <</SYS>>
            
            {user_prompt} [/INST]

            """


    model_inputs = token(
        [complete_prompt], return_tensors="pt",truncation=True, max_length = 1028).to("cuda")
    streamer = TextStreamer(token,skip_prompt=True)
    generated_ids = model.generate(**model_inputs, do_sample=True, max_new_tokens=1000, streamer=streamer)
    # output = token.batch_decode(generated_ids,skip_special_tokens=True)





