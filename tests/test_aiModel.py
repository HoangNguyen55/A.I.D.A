from random import randint
from transformers import AutoModelForCausalLM
from transformers import AutoTokenizer
from transformers import LlamaTokenizer
from transformers import LlamaForCausalLM
from transformers import AutoConfig,TextStreamer, BitsAndBytesConfig
from langdetect import detect, detect_langs
from accelerate.utils import release_memory
from transformers import LogitsProcessorList, MinLengthLogitsProcessor, RepetitionPenaltyLogitsProcessor



while True:
    prompt = "Enter Prompt:"
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
    

    repoid= '/slrmstore/z-common/TunedModel-big'
    

    model = AutoModelForCausalLM.from_pretrained(
        repoid, device_map="auto", load_in_4bit=True, local_files_only=True)
    
    
    token = LlamaTokenizer.from_pretrained(repoid, padding = 'right')


    if ens==False :
        sys_prompt = "You are a nice assistant, answer questions as polite as possible and be correct and do not give emojis."
        if randint(1,2)==2:
            sys_prompt = "You are a nice assistant, answer questions as polite as possible and be correct and do not give emojis."
    else:
        sys_prompt = "You are an assistant, answer questions as condescending, passive-aggressive and mean as possible, but make sure to give correct informations and do not give emojis."

        


    complete_prompt = f"""
                    <s>[INST] <<SYS>>
                    {sys_prompt}
                    <</SYS>>
                    
                    {user_prompt} [/INST]

                    """

    model_inputs = token(
        [complete_prompt], return_tensors="pt",padding= True, truncation=True, max_length = 2048).to("cuda")
    streamer = TextStreamer(token,skip_prompt=True)
    generated_ids = model.generate(**model_inputs, do_sample=True, max_new_tokens=500, streamer=streamer, temperature=0.7,  # Adjusted temperature
    top_k=60,         # Adjusted top-k sampling
    top_p=0.95      # Adjusted top-p (nucleus) sampling
    )

    release_memory(model)





