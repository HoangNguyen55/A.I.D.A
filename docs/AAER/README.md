# API for AI to access external resources (AAER)
This will be an interpreter which parse the AI output for keywords and run the appropriate programs in a shell
replace the special token of the next keyword with the output of the current keyword
i.e, `search youtube url a song | open -`
`search`: will return the first url of the query 'a song'
`open -`: `-` will be replaced and it will become `open 'https//youtube.com/asong'`

This document lists all of the available helper programs for A.I.D.A to interact with the outside world.

## Backend
- [search](./search.txt)

## Client
- open
