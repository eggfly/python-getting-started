# coding: utf-8

from datetime import datetime

from flask import Flask
from flask import render_template
from flask_sockets import Sockets

from views.todos import todos_view

import time

app = Flask(__name__)
sockets = Sockets(app)

# 动态路由
app.register_blueprint(todos_view, url_prefix='/todos')

def bench():
    for i in xrange(1000 * 1000 * 10):
        j = i * 100

@app.route('/')
def index():
    t = time.time()
    bench()
    time_delta = time.time() - t
    return render_template('index.html', time_delta = time_delta)


@app.route('/time')
def get_time():
    return str(datetime.now())


@sockets.route('/echo')
def echo_socket(ws):
    while True:
        message = ws.receive()
        ws.send(message)
