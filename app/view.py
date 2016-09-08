from app import app,db
from flask import render_template,jsonify,request, url_for, json, g , session,request,jsonify,redirect
import pandas as pd
import os
import model

@app.route('/login',methods = ['POST','GET'])
def index():
    return render_template('index.html')




def valid_login(login,password):
    user  = model.Users.query.filter(_and(model.Users.login == login,model.Users.password == password))
    if user:
        return True
    else:
        return False


@app.route('/login/valid',methods = ['POST','GET'])
def check():
    if 'username' in session:
        return jsonify({'responce':"Ok! Your password is valid!"})
    else:
        if valid_login(login = request.json['login'],password=request.json['password']):
            return jsonify({'responce':"Login before use it!!"})
            redirect()

@app.route('/login/register',methods = ['POST','GET'])
def register():
    request_data = request.json
    user = model.Users(login = request_data['login'],password = request_data['password'],first_name = request_data['first_name'],second_name=request_data['second_name'])
    db.session.add(user)
    db.session.commit()
    db.session.close()
    return jsonify({'responce':"Your have successfully registered!"})



@app.route('/index')
    return render_template("index.html")


