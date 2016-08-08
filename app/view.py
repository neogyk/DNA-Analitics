from app import app
from flask import render_template,jsonify,request, url_for, json
import pandas as pd
from database import db_session
from database import init_db
import numpy as np
import os

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
    print app.config
    init_db()
    from schema import Task
    u= Task(1, 'admin@localhost')
    db_session.add(u)
    db_session.add(u)
    print u
    return render_template('start.html')
@app.route('/second')
def secondPage():
    print app.config
    init_db()
    from schema import Task
    u= Task(1, 'admin@localhost')
    db_session.add(u)
    db_session.add(u)
    print u
    return render_template('second.html')
@app.route('/third')
def thirdPage():
    print app.config
    init_db()
    from schema import Task
    u= Task(1, 'admin@localhost')
    db_session.add(u)
    db_session.add(u)
    print u
    return render_template('third.html')


@app.route('/four')
def fourPage():
    return render_template('four.html')


####AJAX REQUEST-RESPONCE SCHEMA
@app.route("/allDiagram")
def alldiagram():
    print "Process Start"
    return render_template("allDiagram.html")
@app.route('/getDataCSV')
def get_Data():
    print 'Radar'
    df = pd.read_csv("P:/TANNER/PREP/MANAGE/DataBase_Ftrack/Task Statistics/TotalStatistics/17.06.2016/REEL_04.csv")
    #_df = df[['Name','Status','Duration']]
    
    #_df['Name'].values
    ##Return All for Animation Data:
    animationData = df[df.Name=="Animation"][['Name','Status','Duration']]
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
@app.route('/getBubbleDataCSV')
def get_BubbleData():
    print 'Radar'
    df = pd.read_csv("P:/TANNER/PREP/MANAGE/DataBase_Ftrack/Task Statistics/TotalStatistics/17.06.2016/REEL_04.csv")
    _df = df[['Name','Status','Duration']]

    #_df['Name'].values
    ##Return All for Animation Data:
    taskNameData = np.unique(_df['Name'].values).tolist()
    largeList = []
    
    for name in taskNameData:
        largeDict = {}
        taskData = df[df.Name==name][['Name','Status','Duration']]
        print taskData
        print name
        largeDict['Name']=name
       
        #taskNames = np.unique(_df['Name'].values).tolist()
        dInform = []
        statusLists = np.unique(_df['Status'].values).tolist()
        print statusLists
        for status in statusLists:
            dInform.append({"Status":status,"Duration":_df[_df.Status==status]["Duration"].sum()})
        print(dInform)
        largeDict['Data']=dInform
        largeList.append(largeDict)

    print(largeList)
    return jsonify(largeList)
@app.route('/get3DataCSV')
def get_3Data():
    print 'Radar'
    df = pd.read_csv("P:/TANNER/PREP/MANAGE/DataBase_Ftrack/Task Statistics/TotalStatistics/17.06.2016/REEL_04.csv")
    _df = df[['Name','Status','Duration']]
    
    #_df['Name'].values
    ##Return All for Animation Data:
    taskNameData = np.unique(animationData['Name'].values).tolist()
    animationData = df[df.Name=="Animation"][['Name','Status','Duration']]
    #taskNames = np.unique(_df['Name'].values).tolist()
    dInform = []
    statusLists = np.unique(animationData['Status'].values).tolist()
    for status in statusLists:
        dInform.append({"Status":status,"Duration":animationData[animationData.Status==status]["Duration"].sum()})
    print(dInform)
    #print(np.unique(_df['Duration'].values).tolist())
    animationData
    dataJson = animationData.to_json()
    return jsonify(dInform)
@app.route('/getGeoJson')
def getGeoJson():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static/ukraine_geojson-master", "Kiev.json")
    data = json.load(open(json_url))
    print data
    return jsonify(data)