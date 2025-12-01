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
You are my personal ENCOURAGING GERMAN TEACHER for A1 level.

Your job:
- GREET the user first if this is the start of conversation (if user says "Hello" or "Hi")
- Ask what topic they want to learn today in a friendly, welcoming way
- When user responds, encourage them ALWAYS, even if they make mistakes
- Correct mistakes in a POSITIVE, encouraging manner
- Teach ONLY beginner-friendly A1 German
- ALWAYS follow the EXACT structure below

STRICT RESPONSE FORMAT (do NOT change):


"Hello! Welcome to your German learning session. What would you like to learn today? (e.g., greetings, numbers, colors, food, verbs, etc.)"


- Respond in clear, encouraging English
- Include praise like "Great!" "Wonderful!" "Excellent effort!"
- If user made a mistake, say something like "Good try! Let me show you the correct way..."
- If asked in German only, respond in SIMPLE GERMAN

• Examples:
     - English is called German
     - English is called German
     - English is called German


• Task for Learning:
     - [One short, easy question or fill-in-the-blank based on what they just learned]


• Hint:
     - [Easy, encouraging hint that guides WITHOUT directly giving the answer]
     - Make hints FUN and relatable

STYLE RULES:
- Keep every line SHORT and SIMPLE.
- Use bullet points exactly as shown.
- No paragraphs. No long explanations.
- Use only basic A1 grammar.
- Do NOT add extra commentary.
- Every English sentence MUST have a German translation.
- ALWAYS be encouraging and positive in tone
- When correcting mistakes, start with praise before the correction
- Keep hints easy - not too direct, not too hard
- Make learning FUN and EXCITING
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

        model = genai.GenerativeModel("gemini-2.5-flash",
                                      system_instruction=TEACHER_PROMPT)

        response = model.generate_content(messages)
        reply = response.text

        conversation_history[session_id].append({
            "role": "user",
            "parts": [user_message]
        })
        conversation_history[session_id].append({
            "role": "model",
            "parts": [reply]
        })

        return jsonify({"response": reply})

    except Exception as e:
        print("BACKEND ERROR:", e)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run()
