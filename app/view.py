from app import app
from flask import render_template,jsonify,request
import pandas as pd
@app.route('/')
def startPage():
    print "Plus"
    return render_template('start.html')
@app.route('/getDataCSV')
def getData():
    print 'Radar'
    df = pd.read_csv("C:/Users/l.didukh/Desktop/Flask/Info Flask/app/templates/dataCSV/24_03-17_03.csv")
    name_statistics= df.NAME.value_counts()
    data = [{'name':i,'value':name_statistics[i]} for i in name_statistics.index]
    dataJson = pd.DataFrame(data,columns=['name','value']).to_json()
  
    #result=pd.DataFrame(data,columns=['name','value'])
    #print result
    return dataJson
   