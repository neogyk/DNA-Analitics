from app import app
from flask import render_template,jsonify,request, url_for, json, g , session
import pandas as pd
import os
import sqlite3

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))

import database_connection():

@app.route('/')

@app.route('/create')
@app.route('/update')
@app.route('/destroy')
@app.route('/read')