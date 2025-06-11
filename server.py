from flask import Flask,render_template,request,session
from uuid import uuid4
from main import process_question
import os

app = Flask(__name__)

app.secret_key = os.getenv("FLASK_SECRET")

# Set a maximum content length for the request
MAX_CONTENT_LENGTH = 3
#if we dont have conv history in session then initialize as an empty array initially so we start recoeding 
def get_conversation_history():
    if 'conversation_history' not in session:
        session['conversation_history'] = []
    return session['conversation_history']

def add_to_conversation_history(question, answer):
    history = get_conversation_history()
    history.append({'question': question, 'answer': answer})
    if len(history) > MAX_CONTENT_LENGTH:
        history.pop(0)
    session['conversation_history'] = history

#for token management we use flask sessions to store conversation like a cookie
@app.route('/',methods = ["GET","POST"])
def index():
    result = None

    if "user_id" not in session:
        session['user_id'] = str(uuid4())
    if request.method == "POST":
        if request.form.get("sign_out", None):
            session.clear()
            return render_template('index.html', result = result)
        question = request.form['question']
        conversation_history = get_conversation_history()
        result = process_question(question)
        add_to_conversation_history(question, result)
    return render_template('index.html', result = result, gmaps_api_key = os.getenv("GPLACE_API_KEY"))


if __name__ == '__main__':
    app.run(debug=True)