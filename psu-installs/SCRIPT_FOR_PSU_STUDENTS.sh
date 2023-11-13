#!/bin/bash

read -p "Enter your psu email without the @psu.edu (i.e, kqn5278): " user

/usr/bin/ssh -t "$user@172.28.200.30" '/usr/bin/bash -c "${curl https://raw.githubusercontent.com/HoangNguyen55/A.I.D.A/main/psu-installs/install-psu-step1.sh}"'
