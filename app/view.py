from app import app,db
from flask import render_template,jsonify,request, url_for, json, g , session,request,jsonify
import pandas as pd
import os
import model

@app.route('/login',methods = ['POST','GET'])
def index():
    return render_template('index.html')


@app.route('/login/valid',methods = ['POST','GET'])
def check():
    print request.json
    if 'username' in session:
        return jsonify({'responce':"Ok! Your password is valid!"})
    else:
        if valid_login(request.json['login'],request.json['password']):
            return jsonify({'responce':"Login before use it!!"})


@app.route('/login/register',methods = ['POST','GET'])
def register():
    request_data = request.json
    user = model.Users(login = request_data['login'],password = request_data['password'],first_name = request_data['first_name'],second_name=request_data['second_name'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'responce':"Your have successfully registered!"})


def valid_login(login,pasword):
    user  = model.Users.query.filter(model.Users.login == login).first()
    if user.password==pasword and user.login == login:
        return True
