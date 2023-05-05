from flask import Flask, render_template, request, redirect, url_for
import openai
import os

app = Flask(__name__)

class IkigaiAgent:
    def __init__(self, model_name="gpt-3.5-turbo"):
        self.model_name = model_name

    def discover_purpose(self, user_input):
        conversation = [
            {"role": "system", "content": "You are an AI agent capable of helping humans discover their ikigai."},
            {"role": "user", "content": user_input}
        ]
        response = openai.ChatCompletion.create(
            engine=self.model_name,
            messages=conversation
        )
        assistant_reply = response['choices'][0]['message']['content']
        return assistant_reply

ikigai_agent = IkigaiAgent()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/discover', methods=['POST'])
def discover():
    user_input = request.form['user_input']
    discovered_purpose = ikigai_agent.discover_purpose(user_input)
    return render_template('result.html', purpose=discovered_purpose)

if __name__ == '__main__':
    openai.api_key = os.getenv("OPENAI_API_KEY")
    app.run(debug=True)
