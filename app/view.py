from app import app
from flask import render_template,jsonify,request, url_for, json, g , session,request
import pandas as pd
import os


@app.route('/login',methods = ['POST','GET'])
def index():
    return render_template('index.html')