# The team
- Hoang Nguyen: [Everything](#team-roles)
- Xiang Liu: [A.I Dev](#team-roles)
- Robert Liam Miller: [AAER Dev, Website Dev](#team-roles)
- Zachary Whitaker: [Everything](#team-roles)
- Mikheil Uglava: [Website Dev, Database dev](#team-roles)

Project Link: https://github.com/HoangNguyen55/A.I.D.A

Communication tools: Discord

# Product Description

## Major Features
A lovely artificial intelligence thats help you in your daily life.

- [ ] AI recieves input and outputs an appropriate responses
    - [ ] Customizable AI behavior with a config file
- [ ] Server with that communicate with client via websocket
    - [ ] A webpage to manage everything
- [ ] Have text to speech read AI responses
- [ ] Run in containers

## Stretch goals

- [ ] Mobile App
- [ ] Text To Speech with emotions
- [ ] Provide source for questions asked

# Requirements

## Functional (Use Cases)
<!-- Template -->
<!-- 1. TASK -->
<!--     1) Actors:  -->
<!--     2) Triggers:  -->
<!--     3) Preconditions:  -->
<!--     4) Postconditions (success scenario):  -->
<!--     5) List of steps (success scenario): -->
<!--     6) Extensions/variations of the success scenario:  -->
<!--     7) Exceptions: failure conditions and scenarios: -->

1. AI connects to the outside world
    1) Actors: AIDA
    2) Triggers: Text input
    3) Preconditions: valid `keywords` wrap in a `|CMD|...|CMD|` block
    4) Postconditions (success scenario): 
        - connect to external site and returns the appropriate responses
    5) List of steps (success scenario):
        - a shell will run `keyword` command
        - `keyword` returns a response
        - AI recieves `keyword` responses
    6) Extensions/variations of the success scenario: 
        - run some internal app that doesn't necessarily connects to the outside world
    7) Exceptions: failure conditions and scenarios:
        - keyword didn't exist, returns error

1. Search on google
    1) Actors: Person
    2) Triggers: Voice Command
    3) Preconditions: "What is ..."
    4) Postconditions (success scenario): 
        - "According to `website` this blah blah blah"
    5) List of steps (success scenario):
        - Feed input to AI
        - AI uses api to ask google the question
        - AI summerize what google gives and read it to user
    6) Extensions/variations of the success scenario: 
        - "`website` said blah blah", "blah blah is what `website` said", etc...
    7) Exceptions: failure conditions and scenarios:
        - no internet connection so can't google questions, something break
1. Answer general questions
    1) Actors: Person
    2) Triggers: Voice Command
    3) Preconditions: "What is ..."
    4) Postconditions (success scenario): 
        - "The answer is..."
    5) List of steps (success scenario):
        - Input is fed to AI
        - It responses with answers
    6) Extensions/variations of the success scenario: 
        - "This thing is...", "it is...", etc...
    7) Exceptions: failure conditions and scenarios:
        - give the wrong information, or it doesn't know.
1. Playing music
    1) Actors: Person
    2) Triggers: Voice Command
    3) Preconditions: "Play this xxx song" or "play this xxxxx artist"
    4) Postconditions (success scenario): 
        - Music plays
    5) Steps: 
        - Feed input to AI
        - AI returns a URL
        - client will automatically open the URL
    6) youtube music url, spotify url, etc...
    7) If the song, album, or the artist can not be found
1. Date reminder
    1) Actors: Person
    2) Triggers: Voice Command
    3) Preconditions: "Hey A.I.D.A remind me to xxxx event on xx date and xx:xx time"
    4) Postconditions (success scenario): 
        - A.I.D.A API will sent the date reminder to Google
    5) List of steps (success scenario):
        - Feed input to AI
        - AIDA calls api to calendar apps to make a reminder
    6) Extensions/variations of the success scenario: 
        - make api call to microsoft calender, etc...
    7) Exceptions: failure conditions and scenarios:
        - Reminder Date and Time that have been past


## Non-Functional

1. Scalability: 
    1) seperate AI memories for different users, so multiple user can use at the same time
    1) new user can sign up to an instance
    1) add more gpus to generate outputs faster
1. Usability:
    1) python Jupyer notebooks to easily run on google collab
    1) install scripts/container to run locally
1. Security:
    1) Encryption of user credentials/data
    1) communicate via TLS

# External Requirements
- [ ] Provide a way to easily install and run it
    - [ ] Provide a way for user to download the AI model we are using.
- [ ] Explain how to build from source
- [ ] Well documented

# Software Architecture
## Components
#### Rust: 
Dependencies:  
- [Reqwest](https://docs.rs/reqwest/latest/reqwest/): simplifies the process of making HTTP requests and handling HTTP responses

#### Python: 
Dependencies:  
- [Websocket](https://websockets.readthedocs.io/en/stable/index.html): facilitate real-time, bidirectional communication between clients and servers.

- [Django](https://www.djangoproject.com/): web framework for building web applications, providing tools for routing, database interactions, authentication, and more.

- [Sqlite3](https://docs.python.org/3/library/sqlite3.html): offers a simple way to work with SQLite databases within Python applications

- [Transformer](https://huggingface.co/docs/transformers/index): enable advanced natural language processing tasks using deep learning techniques.

#### LLM:
- [Llama 2](https://ai.meta.com/llama/): LLM model, responses to user queries.

## Interface
- Python -> Llama 2: use Transformer library to run Llama 2. Llama 2 take in text and output text.
- Llama 2 -> Rust: Llama 2 run the rust compiled program as a commandline application. The AAER app take in text and output text.
- Django -> Database: Django admin webpage will make calls to python functions that can update the database, Django calls python function with input depeneding on the data (change password need text as input) the output would be nothing if the operation succeded otherwise an exception is thrown.
- Websocket -> Llama 2: The websocket server will send the user input into Llama 2 as it come in. websocket recieve text input from the client, and send it to Llama 2 via a python function, then it send the output of Llama 2 back to the client.

## Data
The data being stored are user related data, using for logging, and their admin permission, etc...

Currently there is only one customizable feature that is stored in the database, which is System Prompt.

### Logs
All pass and current conversation are stored in plain text.

### Database
No data is store prior to prompting, data are only store for approved user and user that signup

#### Users
Stores user that can access the app

|id     |usrename   |password |email    |is admin   |last login  |system prompt  |
| -     |-          |-        |-        |-          |-           |-              |
|int    |String     |String   |string   |Bool       |Datetime    |String         |
|...    |...        | ...     |...      |...        |...         |...            |

#### Pending approval
Store user that registered but still need approval from the admin

|username   |password |email    |
|-          |-        |-        |
|String     |String   |string   |
|...        | ...     |...      |

## Assumptions
Hardware: Assume the user have the machine with at least Rtx 4090 Nvidia GPU, 128gb RAM

## Alternatives
#### Rust:
Python:
- Pros: easy to use
- Cons: slow

Go:
- Pros: easy to use, faster than python, fast compile time compare to rust
- Cons: google tracking

#### Websocket:
REST APIs:
- Pros: Easy to implement, and scalable
- Cons: Time lag make it hard for real time communication

Polling:
- Pros: Can be use in case websocket is not available
- Cons: less efficient than Websocket

#### Llama 2:
[TinyLlama](https://huggingface.co/PY007/TinyLlama-1.1B-Chat-v0.3)
- Pros: Less hardware requirements
- Cons: Isn't as good as Llama 2

[OpenAssistant](https://github.com/LAION-AI/Open-Assistant)
- Pros: It already trained for the purpose of virtual assistant so we can use it right away
- Cons: Early stage of development

#### Django:
Flask
- Pros: Simplicity and Minimalism.
- Cons: Flask's minimalism can be a limitation for larger, more complex projects

Express.js
- Pros: Speed and Scalability.
- Cons: Too minimal which make it harder to implement complex task

#### Sqlite3: 
MySQL:
- Pros: More robust, Scalability
- Cons: Complicated to setup

PostgreSQL:
- Pros: Support complex datatype
- Cons: Resource-intensive, Hard to setup

#### Transformer:
Tinygrad:
- Pros: Easy to use
- Cons: Not as easy as Transformer

Pytorch:
- Pros: Powerful
- Cons: Pretty much have to write everything from scratch


# Software Design

### Rust:
Compiled language use for creating commandline programs for the AI to use for communicating with APIs from the internet.
##### Dependencies:
Reqwest: Make APIs calls
- receive url to make REST calls to
- allow user to build header using builder pattern
- recieve response of a website as text so the user can do their own operation on it
- abstract away crafting http calls by hand, headers, handshaking, etc...

### Python:
High-level programming language used running machine learning models.

##### Dependencies:
Websocket: Create a websocket server/client for communicating via text
- recives http headers and parse to make sure it is coming from a valid source
- establish a connection with a client and communicate via text, binary data are also possible
- abstract away handshaking, compressing, websocket protocols, etc...

Django: Create front-end of the admin website
- handle GET request
- serve html pages to the connecting browser
- recieve events coming from the browser (REST)
- abstract away having to write html, server backend codes

Sqlite3: Interface with database for storing user data
- take in data that is compatible to the database and do the corresponding query
- abstract away sql query

Transformer: Easy inferencing LLMs 
- recieve name of LLM to run, download it if there is no local copy
- run the LLM with its corresponding ML algorithm
- abstract away implementation of ML algorithm (RNN, Transformer, etc...)

# Development Processes
## Programing Languages
- Python 
    - Can use the Hugging Face's Transformer library to easily deploy AI models
    - Django as a framework for the admin web page
    - Can be use as backend for servers
- Rust
    - Easily compiles to different OSes
    - Compiles to an executable which is what AIDA will use to interface with the outside world

## Team Roles
- A.I developer (A.I Dev)
    - Data collector
    - Train the A.I and deploy it
- Backend developer (Server Dev)
    - Develope server for client to connect to
- Database Dev
- Frontend developer for admin page (Frontend Dev)
- API for AI to access external resources developer (AAER Dev)
    - Create applications for the AI to access the World Wide Web
- CI/CDer
    - set up ci/cd

## Risks

1. Not having access to a powerful enough computer for running the app:
    - **Likelihood of occurring (high, medium, low)**: Medium
    - **Impact if it occurs (high, medium, low):** High
    - **Evidence upon which you base your estimates, such as what information you have already gathered or what experiments you have done:** We can not access the school computer from the outside for the last two weeks it have been build.
    - **Steps you are taking to reduce the likelihood or impact, and steps to permit better estimates:** Ask Nate daily
    - **Plan for detecting the problem:** Ask Nate daily
    - **Mitigation plan should it occur:** Run on google collab, or rent out a cheap server to run our app

2. Lost of data:
    - **Likelihood of occurring (high, medium, low)**: low
    - **Impact if it occurs (high, medium, low):** medium
    - **Evidence upon which you base your estimates, such as what information you have already gathered or what experiments you have done:** Hoang's SSD broke twice since the school started, he also fries his 3080.
    - **Steps you are taking to reduce the likelihood or impact, and steps to permit better estimates:** Upload code to github, data to the cloud.
    - **Plan for detecting the problem:** Check git status for unpushed commit
    - **Mitigation plan should it occur:** Redo all the lost work

3. The team don't have enough time to work on the project:
    - **Likelihood of occurring (high, medium, low)**: medium
    - **Impact if it occurs (high, medium, low):** medium
    - **Evidence upon which you base your estimates, such as what information you have already gathered or what experiments you have done:** 
        - Hoang is taking 7 class right now and a part-time job
        - Zach have 6 classes and a part-time job
        - Xiang, Mikail have a part-time job.
    - **Steps you are taking to reduce the likelihood or impact, and steps to permit better estimates:** Better time managment.
    - **Plan for detecting the problem:** Everyone in the team checking their available schedules
    - **Mitigation plan should it occur:** Cut down the scope of the project

4. Breaking changes in dependencies:
    - **Likelihood of occurring (high, medium, low)**: low
    - **Impact if it occurs (high, medium, low):** high
    - **Evidence upon which you base your estimates, such as what information you have already gathered or what experiments you have done:** In Hoang testing for Docker build, everything break when the docker image expect CUDA 12.2 but he have 12.0 installed.
    - **Steps you are taking to reduce the likelihood or impact, and steps to permit better estimates:** Regularly testing
    - **Plan for detecting the problem:** Regularly testing 
    - **Mitigation plan should it occur:** Update/downgrade the affected dependencies.

5. Cost changes to API/Library we use:
    - **Likelihood of occurring (high, medium, low)**: low
    - **Impact if it occurs (high, medium, low):** medium
    - **Evidence upon which you base your estimates, such as what information you have already gathered or what experiments you have done:** Recently tech company like Reddit, X (Formerly known as Twitter), update their API cost which make it unreasonable for independent developers to make use of it, github could do the same and make github action cost something.
    - **Steps you are taking to reduce the likelihood or impact, and steps to permit better estimates:** Find alternative APIs, or services
    - **Plan for detecting the problem:** Website sent email when they have cost changes to their service
    - **Mitigation plan should it occur:** Switch to a new service/APIs
    

There was virtually no risk when we first submit our requirement, the only thing we have are 

`The team don't have enough time to learn new technology`

## Schedule
### A.I Dev:
- October 16 - 30: Fine-tune Llama 2 with [dataset](https://huggingface.co/datasets/timdettmers/openassistant-guanaco)

### Backend Dev:
- October 16 - 23: Validate user thats in the database

### Database Dev:
- October 16 - 23: Update database to the current schema

### Frontend Dev:

### AAER
- October 16 - 30 : Create the `search` API

### CICD:
- October 16 - Nov 7: Set up docker build system to package everything thats needed to run the app into 1 container

### Core
Final Deadline: November 12th

## Documentation plan

User guide: Hoang will make a one click install script, and a wikipage for more details

Dev Guide: Update the [CONTRIBUTING.md](CONTRIBUTING.md)

Code documentation: Auto generated from Docstrings with [pydoc](https://docs.python.org/3/library/pydoc.html)

## External Feedback
External feedback would be needed after the AI is up and running, we can ask friends and family.
