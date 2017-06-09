from flask import Flask

app = Flask(__name__)


@app.route('/')
def greetings():
    return 'greetings!'

app.run(port=2333)
