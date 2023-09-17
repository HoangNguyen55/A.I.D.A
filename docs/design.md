# The team
- Hoang Nguyen: [Everything](#team-roles)
- Xiang Liu: [A.I Dev](#team-roles)
- Robert Liam Miller: [AAER Dev, Frontend Dev](#team-roles)
- Zachary Whitaker: [Everything](#team-roles)
- Mikheil Uglava: [Frontend Dev, Database dev](#team-roles)

Project Link: https://github.com/HoangNguyen55/A.I.D.A

Communication tools: Discord

# Product Description

## Major Features
A lovely artificial intelligence thats help you in your daily life.

- [ ] AI recieves input and outputs an appropriate responses
    - [ ] Customizable AI behavior with a config file
- [ ] Server with REST APIs implemented
    - [ ] A webpage to manage everything
- [ ] Have text to speech read AI responses
- [ ] Run in containers

## Stretch goals

- [ ] Mobile App
- [ ] Text To Speech
- [ ] Provide source for questions asked

# Requirements

## Functional (Use Cases)

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

## Schedule

### A.I Dev:
- September 5th - September 13rd: Deploy the A.I (Chat with it like a chat bot via text)
- September 13rd - 27th: Collect Data
- September 27th: Train the A.I (Give desireable output)

### Backend Dev:
- Sep 13rd - 27th: Feed input into the A.I from a REST API
- XXX: Make a database and store something in it

### Frontend Dev:
- September 13rd - 20th: Interface with the A.I

- XXX: Accept User Sign up
- XXX: Button to export the data in the database to csv or something
- XXX: See health of the A.I (optional)
- XXX: See statistic of server usage

### AAER
- September 5th - 27th: Create the `search` API

### Basic core
Soft deadline: September 10th

### Core
Final Deadline: November 12th

## Risks
1. The team don't have enough time to learn new technology

## External Feedback
External feedback would be needed after the AI is up and running, we can ask friends and family.
