# The team
- Hoang Nguyen: Everything
- Xiang Liu: [A.I Dev](#team-roles)
- Robert Liam Miller: [AAER Dev, Frontend Dev](#team-roles)
- Zachary Whitaker: [AAER dev, Backend dev](#team-roles)

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
1. Answer general questions
1. Playing music
1. Date reminder
1. Hand-free command

## Non-Functional

1. Design for 1-4 users per instance
1. Easily run on Google collab/locally
1. Encryption of user credentials/data

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
soft deadline: September 10th

Final Deadline: November 12th

## Risks
Wait till basic core is complete

## External Feedback
External feedback would be needed after the AI is up and running, we can ask friends and family.
