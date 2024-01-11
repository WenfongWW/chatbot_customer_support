from flask import Flask, request, render_template, jsonify 
import openai
from transformers import AutoModelForCausalLM, AutoTokenizer

openai.api_key = "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"

completion = openai

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("chat.html")

@app.route('/get', methods=['GET', 'POST'])
def ticket_form():
    message = request.form["message"]
    input = message
    return get_chatbot_response(input)

#https://huggingface.co/microsoft/DialoGPT-medium?text=Hey+my+name+is+Thomas%21+How+are+you%3F

def get_chatbot_response(text):
    tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
    model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")
# Let's chat for 5 lines
    for step in range(5):
        # encode the new user input, add the eos_token and return a tensor in Pytorch
        new_user_input_ids = tokenizer.encode(input(">> User:") + tokenizer.eos_token, return_tensors='pt')

        # append the new user input tokens to the chat history
        bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids

        # generated a response while limiting the total chat history to 1000 tokens, 
        chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

        # pretty print last ouput tokens from bot
        print("DialoGPT: {}".format(tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)))

