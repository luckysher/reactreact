''' flask app with mongo '''
import os
import json
import datetime
from flask import Flask
from flask import render_template, request
# create the flask object
app = Flask(__name__)


@app.route('/')
def index():
    """ static files serve """
    return render_template('index.html', data={})


@app.route('/save', methods=['GET', 'POST'])
def save():

    name = request.args.get("name")
    age = request.args.get("age")

    return json.dumps({'name': name, 'age': age, 'email': email})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) # Run the app

