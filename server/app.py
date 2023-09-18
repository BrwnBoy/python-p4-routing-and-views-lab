#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
     return '<h1>Python Operations with Flask Routing and Views</h1>'
 
@app.route('/print/<string>')
def print_string(string):
     print(string)
     return f'{string}'

@app.route('/count/<int:num>')
def count(num):
     return '\n'.join([str(i) for i in range(num - 1)])

@app.route('/math/<int:num1>/<string:op>/<int:num2>')
def math(num1, op, num2):
    if op == 'add':
        return str(num1 + num2)
    elif op == 'sub':
        return str(num1 - num2)
    elif op == 'mul':
        return str(num1 * num2)
    elif op == 'div':
        return str(num1 / num2)
    elif op == 'mod':
        return str(num1 % num2)
    else:
        return 'Invalid operation'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
