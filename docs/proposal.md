# Free and open-source Virtual Assistant, A.I.D.A
## Idea
AI assistant that can help with daily tasks, i.e. play music, answer general questions, etc...

## Vision
A Virtual Assistant that can function as good as its proprietary competitors.

## Competitive Analysis
The user have full control over their VA, they can change the system prompt, the TTS engine, etc...

The user own their data, they can turn off telemetry completely.

## Techstack
Python: run the LLM, backend REST APIs
Kotlin: mobile interface 

## Challenge/Risk
The single most serious risk we would face is the fact that our app have three different moving parts, the AI, the mobile app, and the server. Getting another team to build and run this painlessly would be very hard.

The risk can be reduce by:
- Using containers for the server.
- Hardcode in link for downloading LLama2 from Meta's server.
- Android studio can be use to compiles and run the kotlin codes.
