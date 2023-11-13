#!/bin/bash

pipe="/tmp/AIDA_INSTALL_PIPE"
mkfifo "$pipe.in" "$pipe.out"

slurm_path="/slrmstore/$(whoami)/"
step_2="$slurm_path/A.I.D.A/psu-installs/install-psu-step2.sh $(whoami)"

rm -rf A.I.D.A
git clone --depth 1 https://github.com/HoangNguyen55/A.I.D.A
[ -d "$slurm_path/A.I.D.A" ] && rm -rf "$slurm_path/A.I.D.A"
cp -r ./A.I.D.A  $slurm_path

srun --nodes=1 --ntasks-per-node=1 --gres=gpu:1 --time=1:00:00 --pty $step_2
