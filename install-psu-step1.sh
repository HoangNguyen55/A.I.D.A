#!/bin/bash

slurm_path="/slrmstore/$(whomai)/"
step_2="$slurm_path/A.I.D.A/install-psu-step2.sh $(whomai)"

git clone --depth 1 https://github.com/HoangNguyen55/A.I.D.A
cp -r ./A.I.D.A  $slurm_path

srun --nodes=1 --ntasks-per-node=1 --gres=gpu:1 --time=1:00:00 --pty $step_2
