''' flask app with mongo '''
import os
import json
import datetime
from flask import Flask
from flask import render_template, request
# create the flask object
app = Flask(__name__)
