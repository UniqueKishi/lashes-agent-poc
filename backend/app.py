import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# This reads the clean file your ETL pipeline created
def load_clients():
    try:
        with open('clients.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("ERROR: clients.json not found! Did you run etl_pipeline.py?")
        return []

clients_db = load_clients()
print(f"Server started. Loaded {len(clients_db)} clients from database.")


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "").lower()

    # LOGIC A: Check for overdue clients
    if "who hasn’t booked" in question or "fill" in question:
        overdue_clients = []

        # Loop through the REAL data
        for client in clients_db:
            if client["last_visit_days"] > 21: #add a part about the days being less than 60 days so it doesnt reach out to people that were a year ago
                overdue_clients.append(client["name"])

        count = len(overdue_clients)
        
        # Create a dynamic list of names for the response
        # If the list is huge, we might only show the first 3 names to keep it clean
        names_preview = ", ".join(overdue_clients[:3]) 
        if count > 3:
            names_preview += f" and {count - 3} others"

        return jsonify({
            "response": f"You have {count} clients who haven't booked in 3 weeks: {names_preview}. Here’s a message you can send: 'Hi [Name], just checking in! It’s been a few weeks since your last appointment. Want to book your next fill?'"
        })

    # LOGIC B: (Still Hardcoded for now - we will fix this next!)

    elif "aftercare" in question or "tips" in question:
        return jsonify({
            "response": "Here are 3 tips you can use to take care of your lashes:\n• Avoid water and steam for 24 hours\n• Don’t rub or pull your lashes\n• Use oil-free cleanser and brush daily\n\nWant me to save this as a reusable message?"
        })

    elif "save" in question:
        return jsonify({
            "response": "Got it! I’ve saved your aftercare message for future use."
        })

    else:
        return jsonify({
            "response": "I’m here to help with rebooking, reminders, and aftercare tips. What would you like to do?"
        })

if __name__ == "__main__":
    print("Starting Lash Agent backend...")
    app.run(debug=True, port=5001)