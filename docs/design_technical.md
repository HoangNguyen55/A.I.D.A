# AI
Using Meta's [LLama2](https://huggingface.co/blog/llama2) LLM as a base

Deploy using [Transformer](https://huggingface.co/docs/transformers/index)

Fine tunes to output special token when asked specific questions

i.e `"Play me a song" > "search -e youtube -o url a song | open -"`

# Backend
A server that feed input from the client to the AI, perform special actions on the AI's output

Also responsible for validating the users and keep track of user sessions

Perform operations on the database

Generate a URL for the client to connect to this instance

# Client

Send input to the server

# API for AI to access external resources (AAER)
Parse input which is syntactically similar to bash

Execute keywords in chunks, seperated by a pipe

Keywords are just external programs

For a full explaination go [here](./AAER/README.md)

## Backend
Functions like a preprocessor in C

Certain keywords will execute and replace certain tokens in the next chunk with it's output

## Client
Commandline Agruments:
- `--link <url>`: websocket url
- `--port <port>`: port number

i.e: 
`py client.py --link ws://localhost --port 5172 --path login`
= `uri = "ws://localhost:5172/login"`

`py client.py --link ws://localhost --port 5172 --path signup`
= `uri = "ws://localhost:5172/signup"`

Have a loop and take in user input, send it to the server.
When you connect via either login or signup, ask for username and password

i.e:
username = username
password = password

auth = base64encode("username:password")
authorizations = {"Authorization": f"Basic {auth}"}

# Communication between Backend and Client
REST APIs with TLS (stretch goal)

Run in localhost

To access from the internet port forwarding, or [ngrox](https://ngrok.com/) is needed

# Database
SQL database

Store user login details

# CI/CD
uses Jenkins

# Admin Webpage
- let admin see logs
- stop/start AI
