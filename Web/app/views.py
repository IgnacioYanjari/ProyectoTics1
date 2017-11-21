from app import app
from datetime import datetime , time , date
from flask import render_template,request,redirect
import psycopg2

from config import *
conn = psycopg2.connect("dbname=%s host=%s user=%s password=%s"%(database,host,user,password))
cur = conn.cursor()

@app.route('/')
@app.route('/index',methods=['POST'])
def index():
    sql = """ SELECT tipo_agua FROM tipos_aceptados GROUP BY tipo_agua;"""
    cur.execute(sql)
    tipo_agua = cur.fetchall()
    #print(tipo_agua)

    sql="""SELECT nombre_tipo FROM tipos_aceptados """
    cur.execute(sql)
    nombres_aceptados = cur.fetchall()

    if request.method == 'POST':
        return render_template("index.html")


    return render_template("index.html",tipo_agua2 = tipo_agua ,nombres_aceptados = nombres_aceptados)

@app.route('/data',methods=['GET','POST'])
def data():
    if request.method == 'GET':
        temp = request.args['temperatura']
        ph = request.args['ph']
        print("Paquete recibido en : " , datetime.now().second ,"temperatura : ", temp , "ph : " ,ph)
        return render_template("index.html",temperatura=temp,ph=ph)
    return render_template("index.html",temperatura=temp,ph=ph,ec=ec)
