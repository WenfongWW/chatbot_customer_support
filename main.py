
#openai.api_key = "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"

from flask import Flask, render_template, request, jsonify
import openai
import os

# Load the API key from an environment variable
openai.api_key = "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"

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chatbot.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    try:
        # Handling for both GET and POST requests
        msg = request.form.get("msg") if request.method == "POST" else request.args.get("msg")
        if not msg:
            return jsonify({"error": "No message provided"}), 400
        chat_messages = [
            {'role': 'system', 'content': 'You are a IT support.'},
            {'role': 'user', 'content': msg}
        ]
        return get_openai_response(chat_messages)
    except Exception as e:
        app.logger.error(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

@app.errorhandler(500)
def internal_error(exception):
    app.logger.error(exception)
    return "Internal server error", 500

def get_openai_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=100,
    )
    return response.choices[0].message.content

if __name__ == '__main__':
    app.run()
