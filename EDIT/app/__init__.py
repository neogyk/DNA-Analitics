from  flask import Flask,jsonify
import config
app = Flask(__name__)
app.config.from_object(__name__)

import view

