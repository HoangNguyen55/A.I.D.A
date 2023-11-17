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
Press enter, say yes and put in your psu email password

### STEP 4:
Be patiences while its installing, it will take 5-7 minutes to install

### STEP 5:
Sign up, you can use any email

### STEP 6:
Log in, use the email and password you just sign up with.

### STEP 7:
Enter a prompt, ask a question, but be beware

##### As a 'fun' aside, there is a 50% chance for the AI to be nice or really mean, good luck, have fun.
