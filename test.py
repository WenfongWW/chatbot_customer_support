import openai
from flask import Flask, request, jsonify

# Assuming you have set OPENAI_API_KEY in your environment variables
openai.api_key = "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"

app = Flask(__name__)

@app.route("/ask", methods=['POST'])
def ask():
    user_message = request.json.get("message", "")
    
    # Pre-process user_message if necessary
    # ...

    # Send the message to OpenAI API
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=user_message,
      temperature=0.7,
      max_tokens=150
    )

    # Post-process response.choices[0].text if necessary
    # ...

    return jsonify({"response": response.choices[0].text})

if __name__ == '__main__':
    app.run(debug=True)
