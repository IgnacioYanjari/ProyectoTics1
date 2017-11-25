from app import app
from datetime import datetime , time , date
from flask import jsonify,render_template,request,redirect
import psycopg2,random

from config import *
conn = psycopg2.connect("dbname=%s host=%s user=%s password=%s"%(database,host,user,password))
cur = conn.cursor()



@app.route('/')
@app.route('/index',methods=['POST'])
def index():
    sql="""SELECT nombre,id FROM peceras;"""
    cur.execute(sql)
    listas = cur.fetchall()
    return render_template("index.html",lista=listas)


@app.route('/pecera',methods=['POST','GET'])
def pecera():
    sql = """ SELECT tipo_agua FROM tipos_aceptados GROUP BY tipo_agua;"""
    cur.execute(sql)
    tipo_agua = cur.fetchall()
    sql="""SELECT nombre_tipo,tipo_agua FROM tipos_aceptados """
    cur.execute(sql)
    nombres_aceptados = cur.fetchall()
    danger=2
    if request.method == 'POST':
        nombre_send = request.form['nombre_pez']
        tipoagua_send = request.form['tipo_agua']
        tipopez_send = request.form['tipo_pez']
        print("tipo agua : ", tipoagua_send,"tipo pez :",tipopez_send)
        sql=""" SELECT tipo_pez FROM tipos_aceptados WHERE
        tipo_agua = '%s' and nombre_tipo ='%s';"""%(tipoagua_send , tipopez_send)
        print(sql)
        cur.execute(sql)
        danger = cur.fetchall()
        print(danger)
        if len(danger) == 0:
            danger = -1
        elif len(danger) == 1:
            danger = 1
        else:
            danger=2
    return render_template("pecera.html",tipo_agua2 = tipo_agua ,
                        nombres_aceptados = nombres_aceptados,danger=danger)

    return render_template("pecera.html",tipo_agua2 = tipo_agua ,
                        nombres_aceptados = nombres_aceptados,danger=danger)


@app.route('/data',methods=['GET','POST'])
def data():
    global temp
    global ph
    if request.method == 'GET':
        temp = request.args.get('temperatura')
        ph = request.args.get('ph')
        print("Paquete recibido en : " , datetime.now().second ,"temperatura : ", temp , "ph : " ,ph)
        return jsonify(temperatura=temp,ph=ph)
    elif request.method == 'POST':
        return jsonify(temperatura=temp,ph=ph)
    else:
        return jsonify(temperatura=temp,ph=ph)
