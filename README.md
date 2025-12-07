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

- **Frontend**: HTML5, CSS3, JavaScript (Fetch API). Simple UI served via `http.server`
- **Backend**: Python, Flask.
- **Data**: CSV (Source) -> ETL Pipeline -> JSON (Runtime Database).
- **Future**: Designed for integration with booking systems, SMS/email APIs, and time-based triggers

---

## 🚀 How to Run

### Step 1: Open your terminal and clone the repository:

git clone https://github.com/UniqueKishi/lashes-agent-poc.git

cd lashes-agent-poc

### Step 2: Set Up the Virtual Environment

**For Mac/Linux:**

cd backend

python3 -m venv venv

source venv/bin/activate

**For Windows:**

cd backend

python -m venv venv

venv\Scripts\activate

### Step 3: Install Flask (the web server) and CORS (security handler):

pip install flask flask-cors

### Step 4: Initialize the Data (ETL Pipeline)

Run this command inside the backend folder:

python3 etl.py

### Step 5: Start the Server

python3 app.py

Success Message: Server started. Loaded X clients.

### Step 6: Use the App!
Leave the terminal running.

Go to the main folder and double-click index.html to open it in your browser.

---

### Business Value
Lash artists often lose clients due to missed rebooking or poor aftercare. This agent helps:

Increase rebooking rates with timely nudges

Reduce complaints with proactive aftercare

Build trust and retention through consistent communication

### Future Vision
In production, this agent would run automatically:

Triggered 3 weeks after an appointment

Integrated with a booking system (e.g., Square)

Delivering messages via SMS or email (e.g. SendGrid)

Built in Copilot Studio or Azure Logic Apps for no-code automation

---

Author
Kishi Shobowale Business + Tech | Customer Success | Cloud Solution Architect (in progress)


