# This is an installation instruction for PSU students only.

### Prerequisites:
1. Make sure you are on the campus WIFI (or using [GlobalProtect](https://pennstate.service-now.com/sp?id=kb_article_view&sysparm_article=KB0013431))

2. Make sure you have [SSH installed](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui).

### STEP 1:
Open up a terminal (CTRL + Backtick (`) on vscode) or powershell.

### STEP 2:
Copy and paste this command.

Replace `**USER**` with your psu email without the @ (`xyz123` instead of `xyz123@psu.edu`)

`ssh -t "**USER**@172.28.200.30" '/usr/bin/bash -c "$(curl https://raw.githubusercontent.com/HoangNguyen55/A.I.D.A/main/psu-installs/install-psu-step1.sh)"'`


Your complete comand should look like this

`ssh -t "xyz123@172.28.200.30" '/usr/bin/bash -c "$(curl https://raw.githubusercontent.com/HoangNguyen55/A.I.D.A/main/psu-installs/install-psu-step1.sh)"'`

### STEP 3:
Press enter and put in your psu email password

### STEP 4:
Be patiences while its installing
