# -*- coding: utf-8 -*-
# @Time    : 2020/9/10
# @Author  : YifeiDuan
# @Site    : 
# @File    : app.py

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run(debug='true', port=8088)
