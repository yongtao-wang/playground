import os
import sqlite3

from flask import Flask, request, session

import config


app = Flask(__name__)
app.config.from_object(config)
app.debug = False if config.DEV else True


@app.route('/')
def greetings():
    return 'greetings!'


def show_pid():
    return str(os.getpid())
# equals to the route wrapper
app.add_url_rule('/pid/', 'pid', show_pid)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2333)
