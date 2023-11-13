#!/bin/bash
user="$1"
aida_path="/slrmstore/$user/A.I.D.A"
pipeout="/tmp/AIDA_INSTALL_PIPE.out"

model_path="/slrmstore/$user/Llama-2-7b-chat-hf"

start_server="$aida_path/psu-installs/start-server.sh"

start_client="$aida_path/psu-installs/start-client.sh"


tmux new-session -d -s aida-session "$start_server $aida_path"

echo "Wait for installations..."
while ! test -f "/tmp/done"; do
    clear
    cat < "$pipeout" 
    sleep 1
done

rm /tmp/done
tmux split-window -h -t aida-session
tmux send -t aida-session "$start_client $aida_path" ENTER
tmux new-session -A -s aida-session
