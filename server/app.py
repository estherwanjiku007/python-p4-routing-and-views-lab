#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(f"{parameter}")
    return f"{parameter}"

@app.route('/count/<int:parameter>')
def count(parameter):
    my_result = ''
    for i in range(0, parameter):
        my_result += f"{i}\n"
    
    return my_result


@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, num2, operation):
    if operation == '+':
        return f"{num1 + num2}"
    elif operation == '-':
        return f"{num1 - num2}"
    elif operation == '*':
        return f"{num1 * num2}"
    elif operation == '/':
        return f"{num1 / num2}"
    elif operation == 'div':
        return f"{num1 / num2:.1f}"
    elif operation == '%':
        return f"{num1 % num2}"
    else:
        print("Operation not found")
        return f"Operation {operation} is invalid"


if __name__ == '__main__':
    app.run(port=5555, debug=True)