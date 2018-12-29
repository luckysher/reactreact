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

