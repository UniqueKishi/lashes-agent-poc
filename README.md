# Lash Business Automation Agent

## Overview
Solo lash artists and small business service providers often struggle to maintain client engagement between appointments. This lightweight AI assistant shows how many clients have not rebooked in the past 3 weeks so that reminders or check-ins can be sent. It can evolve into an automated agent that sends rebooking reminders, feedback messages, aftercare tips, client preferences, special occasions and product suggestions. All of this helps artists build trust, improve retention, and grow their business.

## Tech Stack
- Python  
- Flask  
- HTML  
- JavaScript  

## Features
- Rebooking reminder flow (“Who hasn’t booked in 3 weeks?”)  
- Aftercare tips flow (“What aftercare tips should I send?”)  
- Product suggestion flow (future vision)  
- Time-triggered automation vision (future vision)

## Architecture
`[Frontend (HTML/JS)] → [Flask Backend] → [Agent Logic]`

- **Frontend**: Simple UI served via `http.server`  
- **Backend**: Flask app with modular intent handling  
- **Future**: Designed for integration with booking systems, SMS/email APIs, and time-based triggers

## Business Value
Lash artists often lose clients due to missed rebooking or poor aftercare. This agent helps:

- Increase rebooking rates with timely nudges  
- Reduce complaints with proactive aftercare messages
- Build trust and retention through consistent communication  

## Future Vision
In production, this agent would run automatically:

- Triggered 3 weeks after an appointment  
- Integrated with a booking system (e.g., Square)  
- Delivering messages via SMS or email  
- Built in Copilot Studio or Azure Logic Apps for no-code automation


## Author
Kishi Shobowale  
Business + Tech | Customer Success | Aspiring Cloud Solution Architect 
