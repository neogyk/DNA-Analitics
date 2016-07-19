from app import app
from flask import render_template,jsonify,request
import pandas as pd
import numpy as np

def diff(list_1,list_2):
    d_list = []
    for i in list_1:
        if i not in list_2:
            d_list.append(i)
    return  d_list
    
def Sum(array):
    sum=0
    for i in array:
        sum+=i
    return sum 
    
@app.route('/')
def startPage():
    print "Plus"
    return render_template('start.html')
@app.route('/getDataCSV')
def get_Data():
    print 'Radar'
    
    df = pd.read_csv("P:/TANNER/PREP/MANAGE/DataBase_Ftrack/Task Statistics/TotalStatistics/17.06.2016/REEL_04.csv")
    #_df = df[['Name','Status','Duration']]
    
    #_df['Name'].values
    ##Return All for Animation Data:
    animationData = df[df.Name=="Rendering"][['Name','Status','Duration']]
    #taskNames = np.unique(_df['Name'].values).tolist()
    dInform = []
    statusLists = np.unique(animationData['Status'].values).tolist()
    for status in statusLists:
        dInform.append({"Name":status,"Duration":animationData[animationData.Status==status]["Duration"].sum()})
    print(dInform)
    #print(np.unique(_df['Duration'].values).tolist())
    animationData
    dataJson = animationData.to_json()
    return jsonify(dInform)

