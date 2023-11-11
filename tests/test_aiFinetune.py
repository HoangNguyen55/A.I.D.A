from os import PathLike
from typing import Any
import logging
import torch
from transformers import AutoModelForCausalLM, AutoConfig, AutoTokenizer, TrainingArguments
from transformers import pipeline
from peft import LoraConfig
from trl import SFTTrainer

# Command to finetune the llama2 in terminal 
#using trl script
python3 /slrmstore/xbl5229/trl/trl/trainer/sft_trainer.py   
    --model_name "/slrmstore/xbl5229/llama2_model"     
    --dataset_name "/slrmstore/xbl5229/OpenassisantDataset"      
    --load_in_4bit     
    --use_peft     
    --batch_size 4     
    --gradient_accumulation_steps 2

# using autotrain
autotrain llm --train --project_name llama2-finetuned \
    --model "/slrmstore/xbl5229/llama2_model" \
    --data_path  "/slrmstore/xbl5229/OpenassisantDataset" \
    --use_peft \
    --use_int4 \
    --learning_rate 2e-8/ \ 
    --train_batch_size 2 \
    --num_train_epochs 6 \
    --trainer sft \
    --model_max_length 4096 \
    --push_to_hub \
    --repo_id xiangliu1123/llama2-openassitant \
    --block_size 4096 > training.log &

