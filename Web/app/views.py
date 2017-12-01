from app import app
from datetime import datetime , time , date
from flask import jsonify,render_template,request,redirect
import psycopg2,random
from app.config import *
conn = psycopg2.connect("dbname=%s host=%s user=%s password=%s"%(database,host,user,password))
cur = conn.cursor()

@app.route('/grafico')
def grafico():
	return render_template('grafico.html')



@app.route('/')
@app.route('/index',methods=['POST','GET'])
def index():
    sql="""SELECT nombre,id,largo,ancho,alto FROM peceras;"""
    cur.execute(sql)
    listas = cur.fetchall()
    if request.method == 'POST':
        nombre_pecera = request.form['nombre_pecera']
        largo_pecera = request.form['Largo']
        ancho_pecera = request.form['Ancho']
        altura_pecera = request.form['quantity']
        exito = 0
        sql = """SELECT nombre FROM peceras WHERE nombre='%s'; """%(nombre_pecera)
        cur.execute(sql)
        nombre = cur.fetchone()
        print (nombre , "nombre_pecera : ", nombre_pecera)
        if nombre == None and len(nombre_pecera) > 0:
            sql = """insert into peceras (nombre, largo, ancho,alto) values (('%s'), ('%s'), ('%s'), ('%s'));
            """%(nombre_pecera,largo_pecera, altura_pecera, ancho_pecera)
            cur.execute(sql)
            conn.commit()
            exito = 1
        sql="""SELECT nombre,id,largo,ancho,alto FROM peceras;"""
        cur.execute(sql)
        listas = cur.fetchall()
        return render_template("index.html",lista=listas, nombre=nombre, exito=exito)

    return render_template("index.html",lista=listas)



@app.route('/pecera/<id_pecera>',methods=['POST','GET'])
def pecera(id_pecera):
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
        tipo_agua = '%s' and nombre_tipo ='%s' and pecera_id = '%s';"""%(tipoagua_send , tipopez_send , id_pecera)
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


@app.route('/peces')
def peces():
    #sql = """select id,tipo_pez,nombre_pez from peces;"""
    #cur.execute(sql)
    #lista_peces = cur.fetchall()
    lista_peces=[["id1","tipo_pez1","nombre_pez1"],["id2","tipo_pez2","nombre_pez2"]]
    return render_template("peces.html",peces=lista_peces)



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
