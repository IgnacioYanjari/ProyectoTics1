from app import app
from datetime import datetime , time , date
from flask import render_template,request,redirect
from config import *
import psycopg2
conn = psycopg2.connect("dbname=%s host=%s user=%s password=%s"%(database,host,user,password))
cur = conn.cursor()

@app.route('/',methods=['GET','POST'])
@app.route('/index',methods=['GET','POST'])
def index():
    temp="fail"
    if request.method == 'GET':
        temp=request.args['temperatura']
        print(" Paquete recivido en : ")
        print(datetime.now())
        print("temperatura")
        print(temp)
        return render_template("index.html",temperatura=temp)
    return render_template("index.html",temperatura=temp)
