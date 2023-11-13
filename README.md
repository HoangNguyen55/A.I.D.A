A.I.D.A, Artificial Intelligence Digital Assistant.

# PSU STUDENT GO [HERE](./psu-installs/INSTALLATION_INSTRUCTIONS.md)


***Linux only tutorial for now***

# Prerequisites
Make sure you have CUDA installed

- [Arch linux](https://wiki.archlinux.org/title/GPGPU#CUDA)
- [Debian](https://wiki.debian.org/NvidiaGraphicsDrivers#Prerequisites)

# Quick Start
Clone the repository:
```
git clone --depth 1 https://github.com/HoangNguyen55/A.I.D.A
cd A.I.D.A
```

Run the scripts:

```
./start-server.sh 'path/to/your/llama2/model'
```

Then on another terminal

```
./start-client.sh
