from config import *
import psycopg2
conn = psycopg2.connect("dbname=%s host=%s user=%s password=%s"%(database,host,user,password))
cur = conn.cursor()

# sql = """ DROP SCHEMA public CASCADE;
# CREATE SCHEMA public;
# """

# cur.execute(sql)

sql = """
CREATE TABLE peces(id serial PRIMARY KEY , tipo_pez integer , nombre_pez varchar, pecera_id int);
CREATE TABLE rangos_peces(tipo_pez integer , ph_max float , ph_min float , temperatura_max float , temperatura_min float);
CREATE TABLE tipos_aceptados(tipo_pez integer , tipo_agua varchar , nombre_tipo varchar);
CREATE TABLE registros_historicos(id serial PRIMARY KEY , fecha timestamp , ph float , temperatura float);
CREATE TABLE peceras(id serial PRIMARY KEY , nombre varchar , largo float , ancho float , alto float);
"""

#queda con 255 el varchar
cur.execute(sql)
conn.commit()
cur.close()
conn.close()
