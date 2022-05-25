import os
from flask import Flask, redirect, request, url_for
import json

app = Flask(__name__)

port = int(os.getenv("PORT", 5501))

def Fibonacci2(n):
    n = int(n)
    if n <= 0:
        #print("Incorrect input")
        return "Enter a Number greater than 0"
        # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci2(n - 1) + Fibonacci2(n - 2)


def Fibonacci(n):
    if n.isdigit():
        x = Fibonacci2(n)
        print("### Fibonacci sequence is {0} .###\n".format(x))
    else:
        x = 'Incorrect Input : Enter a Number greater than 0'
    fib = []
    fib.append({'index': n, 'sequence': x})
    json_data = json.dumps(fib)
    return json_data


@app.route('/fcal', methods=['GET'])
def mediator():
    print("### At Mediator ###\n")
    getindex = request.args.get('fibindex')
    print("### value of getindex is {0} ###".format(getindex))

    return Fibonacci(getindex)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
