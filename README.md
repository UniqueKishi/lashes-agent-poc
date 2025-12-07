# Lash Business Automation Agent 💬

A lightweight AI assistant that helps lash artists rebook clients, send aftercare tips, and improve retention — built with Flask and designed for future automation.

---

## Overview

This proof of concept demonstrates how a solo lash artist can use AI to automate client engagement. The agent handles rebooking reminders, aftercare tips, and product suggestions — all framed around real business value. While this version runs manually, it’s designed for future automation via Copilot Studio or Azure Logic Apps.

---

## ✨ Features

- 🗓️ Rebooking reminder flow (“Who hasn’t booked in 3 weeks?”)
- 💧 Aftercare tips flow (“What aftercare tips should I send?”)
- 🛍️ Product suggestion flow (planned)
- ⏰ Time-triggered automation vision (described below)

---

## 🧱 Architecture
[Frontend (HTML/JS)] → [Flask Backend] → [Agent Logic]

- **Frontend**: Simple UI served via `http.server`
- **Backend**: Flask app with modular intent handling
- **Future**: Designed for integration with booking systems, SMS/email APIs, and time-based triggers

---

## 🚀 How to Run

# Backend
cd backend
python3 -m venv venv
source venv/bin/activate
pip install flask flask-cors
python3 app.py

# Frontend (in separate terminal)
cd ..
python3 -m http.server

Then open http://localhost:8000/index.html in your browser.

##Business Value
Lash artists often lose clients due to missed rebooking or poor aftercare. This agent helps:
Increase rebooking rates with timely nudges
Reduce complaints with proactive aftercare
Build trust and retention through consistent communication

##Future Vision
In production, this agent would run automatically:
Triggered 3 weeks after an appointment
Integrated with a booking system (e.g., Square)
Delivering messages via SMS or email (e.g., Twilio, SendGrid)
Built in Copilot Studio or Azure Logic Apps for no-code automation

Demo Video
[Insert Loom or screen recording link here] Walkthrough of the working flows and business context

Author
Kishi Shobowale Business + Tech | Customer Success | Cloud Solution Architect (in progress)


