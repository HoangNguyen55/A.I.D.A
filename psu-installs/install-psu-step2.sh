#!/bin/bash
user="$1"
aida_path="/slrmstore/$user/A.I.D.A"
pipeout="/tmp/AIDA_INSTALL_PIPE.out"

model_path="/slrmstore/$user/Llama-2-7b-chat-hf"

start_server="$aida_path/psu-installs/start-server.sh"

start_client="$aida_path/psu-installs/start-client.sh"


tmux new-session -d -s aida-session "$start_server $aida_path";             # start a tmux session

echo "Wait for installations..."
while ! test -f "/tmp/done"; do
    clear
    cat < "$pipeout" 
    sleep 1
done

rm /tmp/done
tmux split-window -h;                             # split the detached tmux session
tmux send "$start_client $aida_path" ENTER;                     # send 2nd command 'htop -t' to 2nd pane. I believe there's a `--target` option to target specific pane.
tmux a;                                        # open (attach) tmux session.
