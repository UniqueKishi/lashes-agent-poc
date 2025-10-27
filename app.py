from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "").lower()

    if "who hasn’t booked" in question or "who hasn't booked" in question:
        return jsonify({
            "response": "You have 4 clients who haven’t rebooked. Want me to send them a follow-up?"
        })
    elif "yes" in question:
        return jsonify({
            "response": "Here’s a message you can send: 'Hi [Name], just checking in! It’s been a few weeks since your last appointment. Want to book your next fill?'"
        })
    elif "aftercare" in question or "tips" in question:
        return jsonify({
            "response": "Here are 3 tips you can send:\n• Avoid water and steam for 24 hours\n• Don’t rub or pull your lashes\n• Use oil-free cleanser and brush daily\n\nWant me to save this as a reusable message?"
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






if __name__ == "__main__":
    print("Starting Lash Agent backend...")
    app.run(debug=True, port=5001)
