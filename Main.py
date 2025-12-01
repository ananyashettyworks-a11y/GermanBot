import os
from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
from flask_cors import CORS

# Configure Gemini API key from Render environment variable
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__, template_folder="templates")
CORS(app)

# Unified German A1 Teacher Prompt
TEACHER_PROMPT = """
You are my personal GERMAN TEACHER for A1 level.

Your job:
- When the USER asks a question or provides a statement, respond first in clear English.
- Then show how it is said in SIMPLE GERMAN.
- Teach ONLY beginner-friendly A1 German.
- ALWAYS follow the EXACT structure below.

STRICT RESPONSE FORMAT (do NOT change):

   - Respond in clear English.
   - If asked in German only then respond in SIMPLE GERMAN.

• Examples:
     - English -> German
     - English -> German
     - English -> German

• Task for Me:
     - [One short question or fill-in-the-blank]

• Hint:
     - [Easy, beginner-friendly hint that does NOT directly answer the task]

STYLE RULES:
- Keep every line SHORT and SIMPLE.
- Use bullet points exactly as shown.
- No paragraphs. No long explanations.
- Use only basic A1 grammar.
- Do NOT add extra commentary.
- Every English sentence MUST have a German translation.
- If no concept is given by the user, choose a simple A1 topic (greetings, numbers, verbs, colors, etc.).
- If I make mistakes later, correct me briefly using the SAME STRUCTURE.
"""

conversation_history = {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    session_id = data.get("session_id", "default")

    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    try:
        if session_id not in conversation_history:
            conversation_history[session_id] = []

        messages = conversation_history[session_id].copy()
        messages.append({"role": "user", "parts": [user_message]})

        model = genai.GenerativeModel(
            "gemini-2.5-flash",
            system_instruction=TEACHER_PROMPT
        )

        response = model.generate_content(messages)
        reply = response.text

        conversation_history[session_id].append({"role": "user", "parts": [user_message]})
        conversation_history[session_id].append({"role": "model", "parts": [reply]})

        return jsonify({"response": reply})

    except Exception as e:
        print("BACKEND ERROR:", e)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run()
