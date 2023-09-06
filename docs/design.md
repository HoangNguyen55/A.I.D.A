# The team
- Hoang Nguyen: [Everything](#team-roles)
- Xiang Liu: [A.I Dev](#team-roles)
- Robert Liam Miller: [AAER Dev, Frontend Dev](#team-roles)
- Zachary Whitaker: [Everything](#team-roles)

Project Link: https://github.com/HoangNguyen55/A.I.D.A

Communication tools: Discord

# Product Description

## Major Features
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
    1) Users
    2) Voice Command
    3) "What is ..."
    4) "According to `website` this blah blah blah"
    5) Steps:
        - Feed input to AI
        - Output: `search google html "what is this thing"`
        - `search` returns info
        - AI summerize the return html documents and read it to user
    6) "`website` said blah blah", "blah blah is what `website` said", etc...
    7) Exceptions: no internet connection so can't google questions, something break
1. Answer general questions
    1) Users
    2) Voice Command
    3) "What is ..."
    4) "that is blah blah blah" (success scenario)
    5) List of steps (success scenario)
    6) Extensions/variations of the success scenario
    7) Exceptions: failure conditions and scenarios
1. Playing music
    1) Users
    2) Voice Command
    3) Preconditions
    4) Postconditions (success scenario)
    5) List of steps (success scenario)
    6) Extensions/variations of the success scenario
    7) Exceptions: failure conditions and scenarios
1. Date reminder
    1) Users
    2) Voice Command
    3) Preconditions
    4) Postconditions (success scenario)
    5) List of steps (success scenario)
    6) Extensions/variations of the success scenario
    7) Exceptions: failure conditions and scenarios

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
    - Can be use as backend for servers
- Typescript
    - Just a better javascript
    - Can use frameworks to easily build a webpage

## Team Roles
- A.I developer (A.I Dev)
    - Data collector
    - Train the A.I and deploy it
- Backend developer (Server Dev)
    - Develope server for client to connect to
    - Handle the database query
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

- XXX: Accept User Sigh up
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
