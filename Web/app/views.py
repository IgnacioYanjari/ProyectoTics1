from app import app
from datetime import datetime
from flask import render_template,request,redirect
from config import *
import psycopg2
import time
import serial

conn = psycopg2.connect("dbname=%s host=%s user=%s password=%s"%(database,host,user,password))
cur = conn.cursor()

@app.route('/')
@app.route('/index',methods=['POST','GET'])
def index():
    temp = ""
    if request.method == 'GET':
        temp=request.args['temperatura']
        print ("Temperatura : ")
        print(temp)
        return render_template("index.html",temperatura=temp)
    return render_template("index.html",temperatura=temp)
