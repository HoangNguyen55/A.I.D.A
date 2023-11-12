#!/bin/bash
test="/home/kqn5278/Llama-2-7b-chat-hf"
user="$1"
aida_path="/slrmstore/$user/A.I.D.A"
model_path="/slrmstore/z-common/llama/"
start_server="$aida_path/start-server.sh -m $model_path --auto-approve-signup --inference-on-startup -v"
start_client="$aida_path/start-client.sh"

tmux new-session -d -s aida-session "$start_server";             # start a tmux session
tmux split-window -h;                             # split the detached tmux session
tmux send "$start_client" ENTER;                     # send 2nd command 'htop -t' to 2nd pane. I believe there's a `--target` option to target specific pane.
tmux a;                                        # open (attach) tmux session.
