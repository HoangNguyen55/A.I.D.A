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
Do special action depending on the keywords

# Communication between Backend and Client
REST APIs with TLS (stretch goal)

Run in localhost

To access from the internet port forwarding, or [ngrox](https://ngrok.com/) is needed

# Database
SQL database

Store user login details

# Admin Webpage
