from app import app
from datetime import datetime , time , date
from flask import jsonify,render_template,request,redirect
import psycopg2,random
from app.config import *
conn = psycopg2.connect("dbname=%s host=%s user=%s password=%s"%(database,host,user,password))
cur = conn.cursor()
elevationData = [
    [0.0, 13],
    [0.1, 14],
    [0.2, 16],
    [0.3, 12],
    [0.4, 13],
    [0.5, 15],
    [0.6, 12],
    [0.7, 19],
    [0.8, 11],
    [0.9, 13],
    [1.0, 9],
    [1.1, 10],
    [1.2, 8],
    [1.3, 13],
    [1.4, 15],
    [1.5, 18],
    [1.6, 20],
    [1.7, 30],
    [1.8, 15],
    [1.9, 15],
    [2.0, 13],
    [2.1, 15],
    [2.2, 10],
    [2.3, 15],
    [2.4, 16],
    [2.5, 16],
    [2.6, 15],
    [2.7, 20],
    [2.8, 15],
    [2.9, 10],
    [3.0, 20],
    [3.1, 17],
    [3.2, 15],
    [3.3, 10],
    [3.4, 12],
    [3.5, 12],
    [3.6, 15],
    [3.7, 16],
    [3.8, 14],
    [3.9, 15],
    [4.0, 12],
    [4.1, 15],
    [4.2, 15],
    [4.3, 15],
    [4.4, 17],
    [4.5, 17],
    [4.6, 15],
    [4.7, 17],
    [4.8, 20],
    [4.9, 15],
    [5.0, 10],
    [5.1, 17],
    [5.2, 20],
    [5.3, 15],
    [5.4, 16],
    [5.5, 15],
    [5.6, 20],
    [5.7, 12],
    [5.8, 15],
    [5.9, 20],
    [6.0, 15],
    [6.1, 12],
    [6.2, 16],
    [6.3, 15],
    [6.4, 10],
    [6.5, 13],
    [6.6, 15],
    [6.7, 16],
    [6.8, 20],
    [6.9, 12],
    [7.0, 15],
    [7.1, 10],
    [7.2, 13],
    [7.3, 15],
    [7.4, 12],
    [7.5, 15],
    [7.6, 16],
    [7.7, 19],
    [7.8, 20],
    [7.9, 15],
    [8.0, 15],
    [8.1, 15],
    [8.2, 16],
    [8.3, 17.6],
    [8.4, 15],
    [8.5, 17],
    [8.6, 14],
    [8.7, 15],
    [8.8, 12],
    [8.9, 11],
    [9.0, 10],
    [9.1, 15],
    [9.2, 12],
    [9.3, 19],
    [9.4, 15],
    [9.5, 11],
    [9.6, 13],
    [9.7, 19],
    [9.8, 14],
    [9.9, 12],
    [10.0, 12],
    [10.1, 13],
    [10.2, 14],
    [10.3, 16],
    [10.4, 17],
    [10.5, 13],
    [10.6, 23],
    [10.7, 13],
    [10.8, 14],
    [10.9, 14],
    [11.0, 14],
    [11.1, 15],
    [11.2, 14],
    [11.3, 14],
    [11.4, 14],
    [11.5, 14],
    [11.6, 13],
    [11.7, 14],
    [11.8, 14],
    [11.9, 14],
    [12.0, 11],
    [12.1, 15],
    [12.2, 15],
    [12.3, 13],
    [12.4, 13],
    [12.5, 13],
    [12.6, 18],
    [12.7, 16],
    [12.8, 22],
    [12.9, 23]
]


@app.route('/grafico')
def grafico(chartID = 'chart_ID', chart_type = 'area', chart_height = 500):
	chart = {"renderTo": chartID, "type": chart_type, "height": chart_height , "zoomType" : 'x' , "panning" : 'true' , "panKey": 'shift'}
	series = [{"name": 'Label1', "data":elevationData}]
	title = {"text": 'Intento numero 1 de gráfico'}
	xAxis = {"title":{"text":'Meses Del año'} ,"categories":{"text" : ''}}
	yAxis = {"title": {"text": 'Prueba Y'}}
	return render_template('grafico.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)



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
