import os
from flask import Flask, redirect, request, render_template, url_for
import requests
import json

app = Flask(__name__, template_folder='template')

session = requests.Session()
session.trust_env = False

port = int(os.getenv("PORT", 5500))

@app.route('/fcal', methods=['POST'])
def mediator():
    getindex = request.form['fibindex']
    print("### Find Fibonacci sequence for index {0} .###".format(getindex))

    # CONNECTION with other app
    url = 'http://fibonacci-app-service:5501/fcal?fibindex=' + str(getindex)
    try:
        r = session.get(url=url)
        print(r.status_code)
        print(r.text)
        res = json.loads(r.text)
        for i in res:
            # print i['index']
            n = i['index']
            # print i['sequence']
            x = i['sequence']
        return render_template('output.html', indexnum=n, answer=x)
    except:
        print('Connecting Error or Bad Response from Fibonacci Calculator')
        return render_template('error.html')


@app.route('/recalc', methods=['POST'])
def default_route():
    #type = request.args.get('type')
    #print "### type is {0} ###".format(type)
    return render_template('index.html')


@app.route('/')
def default_route2():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)

