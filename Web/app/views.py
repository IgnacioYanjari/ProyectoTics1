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
    if request.method == 'GET':
        temp=request.args['temperatura']
        ph = request.args['ph']
        ec = request.args['ec']
        #print ' Paquete recivido en :  %s.' % datetime.now()
        #print 'temperatura %s pH %s Ec %s' %temp,%ph,%ec
        print("Paquete recibido en : ")
        print(datetime.now())
        print("temperatura : ")
        print(temp)
        print("ph : ")
        print(ph)
        print("ec : ")
        print(ec)
        return render_template("index.html",temperatura=temp,ph=ph,ec=ec)
    return render_template("index.html",temperatura=temp,ph=ph,ec=ec)
