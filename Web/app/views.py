from app import app
from flask import jsonify,render_template,request,redirect
from datetime import datetime , time , date
import psycopg2,random,time
from app.config import *
conn = psycopg2.connect("dbname=%s host=%s user=%s password=%s"%(database,host,user,password))
cur = conn.cursor()

@app.route('/')
@app.route('/index',methods=['POST','GET'])
def index():
    sql="""SELECT nombre,id,galones, litros FROM peceras;"""
    cur.execute(sql)
    listas = cur.fetchall()
    if request.method == 'POST':
        nombre_pecera = request.form['nombre_pecera']
        capacidad = request.form['capacidad']
        opcion_capacidad = request.form['opcion_capacidad']
        galones_pecera = 0
        litros_pecera = 0
        if opcion_capacidad == "Litros":
            galones_pecera = float(capacidad) / 3.78541
            litros_pecera = float(capacidad)
        else:
            litros_pecera = float(capacidad) * 3.78541
            galones_pecera = float(capacidad)
        exito = 0
        sql = """SELECT nombre FROM peceras WHERE nombre='%s'; """%(nombre_pecera)
        cur.execute(sql)
        nombre = cur.fetchone()
        print (nombre , "nombre_pecera : ", nombre_pecera)

        if nombre == None and len(nombre_pecera) > 0:
            galones_pecera = round(galones_pecera,2)
            litros_pecera = round(litros_pecera,2)
            sql = """insert into peceras (nombre, galones, litros) values (('%s'), ('%s'), ('%s'));
            """%(nombre_pecera,galones_pecera, litros_pecera)
            cur.execute(sql)
            conn.commit()
            exito = 1

        sql="""SELECT nombre,id,galones,litros FROM peceras;"""
        cur.execute(sql)
        listas = cur.fetchall()
        return render_template("index.html",lista=listas, nombre=nombre, exito=exito)

    return render_template("index.html",lista=listas)



@app.route('/pecera/<id_pecera>',methods=['POST','GET'])
def pecera(id_pecera):
    sql = """SELECT fecha , temperatura FROM registros_historicos;"""
    cur.execute(sql)
    datos_temperatura=cur.fetchall()
    sql = """SELECT fecha , temperatura FROM registros_historicos;"""
    cur.execute(sql)
    datos_ph = cur.fetchall()
    aux = []
    for elem in datos_temperatura:
        aux2 = [int(time.mktime(elem[0].timetuple()) * 1000),elem[1]]
        aux.append(aux2)
    datos_temperatura = aux
    aux = []
    for elem in datos_ph:
        aux2 = [int(time.mktime(elem[0].timetuple()) * 1000),elem[1]]
        aux.append(aux2)
    datos_ph = aux
    print("datos_temperatura : ",datos_temperatura)
    print("datos_ph : " , datos_ph)
    return render_template("pecera.html" , datos_temperatura = datos_temperatura , datos_ph = datos_ph)


@app.route('/peces/<id_pecera>',methods=['POST','GET'])
def peces(id_pecera):
#lista_peces=[["id1","tipo_pez1","nombre_pez1"],["id2","tipo_pez2","nombre_pez2"]]
    sql = """select peces.id,tipos_aceptados.nombre_tipo,peces.nombre_pez from peces,tipos_aceptados where  tipos_aceptados.tipo_pez = peces.tipo_pez;"""
    cur.execute(sql)
    lista_peces = cur.fetchall()
    sql = """ SELECT tipo_agua FROM tipos_aceptados GROUP BY tipo_agua;"""
    cur.execute(sql)
    tipo_agua = cur.fetchall()
    sql="""SELECT nombre_tipo,tipo_agua FROM tipos_aceptados;"""
    cur.execute(sql)
    nombres_aceptados = cur.fetchall()
    sql ="""SELECT litros_disponibles FROM peceras WHERE peceras.id='1'"""
    cur.execute(sql)
    litros_disponibles = cur.fetchone()
    danger=2
    if request.method == 'POST':
        nombre_send = request.form['nombre_pez']
        tipopez_send = request.form['tipo_pez']

        ############################################### INGRESAR RANGOS CORRECTOS DE PH ####################################
        sql="""SELECT rangos_peces.ph_min FROM rangos_peces, peces WHERE peces.tipo_pez=rangos_peces.tipo_pez;"""
        cur.execute(sql)
        list_min = cur.fetchall()  #maximo de los minimos ph tenemos que calcular

        max_elem = 0

        for i in list_min:
            if max_elem < i[0]:
                max_elem = i[0]
        sql="""SELECT rangos_peces.ph_max FROM rangos_peces, peces WHERE peces.tipo_pez=rangos_peces.tipo_pez;"""
        cur.execute(sql)
        list_max = cur.fetchall() #minimo de los maximos ph tenemos que calcular

        min_elem = 200
        for i in list_max:
            if min_elem > i[0]:
                min_elem = i[0]

        sql="""SELECT rangos_peces.ph_min FROM rangos_peces,tipos_aceptados WHERE tipos_aceptados.nombre_tipo = '%s' and rangos_peces.tipo_pez=tipos_aceptados.tipo_pez;"""%(tipopez_send)
        cur.execute(sql)
        rango_min = cur.fetchone()

        sql="""SELECT rangos_peces.ph_max FROM rangos_peces, tipos_aceptados WHERE tipos_aceptados.nombre_tipo = '%s' and rangos_peces.tipo_pez=tipos_aceptados.tipo_pez"""%(tipopez_send)
        cur.execute(sql)
        rango_max = cur.fetchone()

############################################### INGRESAR RANGOS CORRECTOS DE TEMPERATURA ####################################

        sql="""SELECT rangos_peces.temperatura_min FROM rangos_peces, peces WHERE peces.tipo_pez=rangos_peces.tipo_pez;"""
        cur.execute(sql)
        list_min2 = cur.fetchall()  #maximo de los minimos ph tenemos que calcular

        max_elem2 = 0

        for i in list_min2:
            if max_elem2 < i[0]:
                max_elem2 = i[0]
        sql="""SELECT rangos_peces.temperatura_max FROM rangos_peces, peces WHERE peces.tipo_pez=rangos_peces.tipo_pez;"""
        cur.execute(sql)
        list_max2 = cur.fetchall() #minimo de los maximos ph tenemos que calcular

        min_elem2 = 200
        for i in list_max2:
            if min_elem2 > i[0]:
                min_elem2 = i[0]

        sql="""SELECT rangos_peces.temperatura_min FROM rangos_peces,tipos_aceptados WHERE tipos_aceptados.nombre_tipo = '%s' and rangos_peces.tipo_pez=tipos_aceptados.tipo_pez;"""%(tipopez_send)
        cur.execute(sql)
        rango_min2 = cur.fetchone()

        sql="""SELECT rangos_peces.temperatura_max FROM rangos_peces, tipos_aceptados WHERE tipos_aceptados.nombre_tipo = '%s' and rangos_peces.tipo_pez=tipos_aceptados.tipo_pez"""%(tipopez_send)
        cur.execute(sql)
        rango_max2 = cur.fetchone()


        sql="""SELECT litros, litros_disponibles FROM peceras WHERE peceras.id = '%s';"""%(id_pecera)
        cur.execute(sql)
        litros_total = cur.fetchone()

        sql="""SELECT litros_de_pez FROM tipos_aceptados WHERE tipos_aceptados.nombre_tipo = '%s' ;"""%(tipopez_send)
        cur.execute(sql)
        litros_pez_ingresado = cur.fetchone()
####
        if litros_total[1] >= litros_pez_ingresado[0]:
            if (rango_min[0]>= max_elem and rango_min[0] <= min_elem) or (rango_max[0]<= min_elem and rango_max[0] >= max_elem) and (rango_min2[0]>= max_elem2 and rango_min2[0] <= min_elem2) or (rango_max2[0]<= min_elem2 and rango_max2[0] >= max_elem2):
                print("tipo pez :",tipopez_send)
                sql=""" SELECT tipo_pez FROM tipos_aceptados WHERE nombre_tipo ='%s';"""%(tipopez_send)
                print(sql)
                cur.execute(sql)
                danger = cur.fetchone()
                for i in range(1,10):
                    print(danger)
                if len(danger) == 0 or nombre_send == "":
                    danger = -1
                elif len(danger) == 1:
######
                    sql="""UPDATE peceras SET litros_disponibles= '%s' WHERE peceras.id = '%s';"""%(litros_total[1]-litros_pez_ingresado[0],id_pecera)
                    cur.execute(sql)
                    for i in range(0,20):
                        print("LITROS TOTAL:", litros_total,"  LITROS DISPONIBLES:", litros_total[1]-litros_pez_ingresado[0])
######
                    sql="""insert into peces(tipo_pez,nombre_pez,pecera_id) values('%s','%s','1');"""%(danger[0],nombre_send)
                    cur.execute(sql)
                    conn.commit()
                    sql = """select peces.id,tipos_aceptados.nombre_tipo,peces.nombre_pez from peces,tipos_aceptados where  tipos_aceptados.tipo_pez = peces.tipo_pez;"""
                    cur.execute(sql)
                    lista_peces = cur.fetchall()
                    danger=1
                else:
                    danger=2

                sql ="""SELECT litros_disponibles FROM peceras WHERE peceras.id='1'"""
                cur.execute(sql)
                litros_disponibles = cur.fetchone()
                return render_template("peces.html",tipo_agua2 = tipo_agua ,nombres_aceptados = nombres_aceptados,danger=danger,peces=lista_peces,litros_disponibles=litros_disponibles)
            else:
                sql ="""SELECT litros_disponibles FROM peceras WHERE peceras.id='1'"""
                cur.execute(sql)
                litros_disponibles = cur.fetchone()
                danger=-2
                return render_template("peces.html",tipo_agua2 = tipo_agua ,nombres_aceptados = nombres_aceptados,danger=danger,peces=lista_peces,litros_disponibles=litros_disponibles)
    return render_template("peces.html",tipo_agua2 = tipo_agua ,nombres_aceptados = nombres_aceptados,danger=danger,peces=lista_peces,litros_disponibles=litros_disponibles)


@app.route('/delete/<id>',methods=['GET','POST'])
def delete(id):

    sql ="""SELECT tipo_pez FROM peces WHERE id = '%s' AND pecera_id ='1';"""%(id)
    cur.execute(sql)
    tipo_pez = cur.fetchone()

    sql = """delete from peces where id ='%s' ;"""%(id)
    cur.execute(sql)

    #for i in range(0,10):
    #    print(tipo_pez)

######
    sql="""SELECT litros_de_pez FROM tipos_aceptados WHERE tipos_aceptados.tipo_pez = '%s' ;"""%(tipo_pez[0])
    cur.execute(sql)
    litros_de_pez = cur.fetchone()

    #for i in range(0,10):
    #    print("LITROS DE PEZ:",litros_de_pez)

    sql = """UPDATE peceras SET litros_disponibles= litros_disponibles + '%s' WHERE peceras.id = '1';"""%(litros_de_pez[0])
    cur.execute(sql)
    conn.commit()

    sql = """SELECT litros_disponibles FROM peceras WHERE peceras.id='1';"""
    cur.execute(sql)
    litros_disponibles = cur.fetchone()

    #for i in range(0,10):
        #print("LITROS DISPONIBLES:",litros_disponibles[0])
    return redirect(request.referrer)



@app.route('/data',methods=['GET','POST'])
def data():
    global temp
    global ph
    if request.method == 'GET':
        temp = request.args.get('temperatura')
        ph = request.args.get('ph')
        fecha = datetime.now()
        print("Paquete recibido en : " , datetime.now(),"temperatura : ", temp , "ph : " ,ph)
        sql = """INSERT INTO registros_historicos(fecha,ph,temperatura) values(('%s'),('%s'),('%s'))"""%(fecha,ph,temp)
        cur.execute(sql)
        conn.commit()
        return jsonify(temperatura=temp,ph=ph,fecha=fecha)
    elif request.method == 'POST':
        return jsonify(temperatura=temp,ph=ph)
    else:
        return jsonify(temperatura=temp,ph=ph)
