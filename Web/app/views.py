from app import app
from datetime import datetime , time , date
from flask import render_template,request,redirect
#from config import *
#import psycopg2
#conn = psycopg2.connect("dbname=%s host=%s user=%s password=%s"%(database,host,user,password))
#cur = conn.cursor()

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/data',methods=['GET','POST'])
def data():
    if request.method == 'GET':
        temp = request.args['temperatura']
        ph = request.args['ph']
        print("Paquete recibido en : " , datetime.now().second ,"temperatura : ", temp , "ph : " ,ph)
        return render_template("index.html",temperatura=temp,ph=ph)
    return render_template("index.html",temperatura=temp,ph=ph,ec=ec)
