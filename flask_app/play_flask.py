import os
import sqlite3

from flask import Flask, request, session

import config


app = Flask(__name__)
app.config.from_object(config)


def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])

@app.route('/')
def greetings():
    return 'greetings!'

app.run(port=2333)
