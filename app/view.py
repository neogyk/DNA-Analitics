from app import app
from flask import render_template,jsonify
import pandas as pd
@app.route('/')
@app.route('/index')
def startPage():
    print "Plus"
    return render_template('start.html')
@app.route('/getDataCSV')
def getDataCSV():
    df = pd.read_csv('templates/dataCSV/24_03-17_03.csv')
    dataJson = df.to_json()
    print 'Radar'
    return dataJson
   