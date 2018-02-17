import os
import sqlite3

from flask import Flask, request, session, redirect, url_for

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


# @app.route('/admin')
def greeting_admin():
  return 'greetings, admin'
app.add_url_rule('/admin', 'admin', greeting_admin, methods=['GET', 'POST'])


def greeting_guest(guest):
  return 'greetings, %s as guest' % guest
app.add_url_rule('/guest/<guest>', 'guest_visit', greeting_guest)


@app.route('/login/<name>', methods=['POST', 'GET'])
def login(name):
  if name == 'admin':
    return redirect(url_for('admin'))
  else:
    return redirect(url_for('guest_visit', guest=name))


@app.route('/user/<name>')
def show_name(name):
    if name != 'me':
        pass
    return 'user name is %s' % name


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2333)
