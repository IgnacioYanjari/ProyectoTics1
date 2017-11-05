from config import *
from datetime import datetime
import psycopg2

conn = psycopg2.connect("dbname=%s host=%s user=%s password=%s"%(database,host,user,password))
cur = conn.cursor()


# Crear Datos Esturión
sql = """
insert into rangos_peces (tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min) values ('1','7,6','7.4','18','10')
returning
tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min;
"""
cur.execute(sql)
conn.commit()

sql="""
insert into tipos_aceptados (tipo_pez , nombre_pez , tipo_agua) values
('1','Esturión','Tropical')
returning
tipo_pez , nombre_pez , tipo_agua;
"""
cur.execute(sql)
conn.commit()


# Crear Datos Cardenal
sql = """
insert into rangos_peces (tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min) values ('2','6,2','5,8','27','23')
returning
tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min;
"""
cur.execute(sql)
conn.commit()
sql="""
insert into tipos_aceptados (tipo_pez , nombre_pez , tipo_agua) values
('2','Cardenal','Tropical')
returning
tipo_pez , nombre_pez , tipo_agua;
"""
cur.execute(sql)
conn.commit()



# Crear Datos Monjita
sql = """
insert into rangos_peces (tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min) values ('3','8,5','5,8','26','20')
returning
tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min;
"""
cur.execute(sql)
conn.commit()
sql="""
insert into tipos_aceptados (tipo_pez , nombre_pez , tipo_agua) values
('3','Monjita','Tropical')
returning
tipo_pez , nombre_pez , tipo_agua;
"""
cur.execute(sql)
conn.commit()


# Crear Datos Tetra de cabeza roja
sql = """
insert into rangos_peces (tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min) values ('4','7,8','7,3','26','23')
returning
tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min;
"""
cur.execute(sql)
conn.commit()
sql="""
insert into tipos_aceptados (tipo_pez , nombre_pez , tipo_agua) values
('4','Tetra de cabeza roja','Tropical')
returning
tipo_pez , nombre_pez , tipo_agua;
"""
cur.execute(sql)
conn.commit()


# Crear Datos Barbo Tetrazona
sql = """
insert into rangos_peces (tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min) values
('5','6,6','6,6','26','20')
returning
tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min;
"""
cur.execute(sql)
conn.commit()
sql="""
insert into tipos_aceptados (tipo_pez , nombre_pez , tipo_agua) values
('5','Barbo Tetrazona','Tropical')
returning
tipo_pez , nombre_pez , tipo_agua;
"""
cur.execute(sql)
conn.commit()


# Crear Datos Danio Cebra
sql = """
insert into rangos_peces (tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min) values
('6','7,0','6,5','24','18')
returning
tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min;
"""
cur.execute(sql)
conn.commit()
sql="""
insert into tipos_aceptados (tipo_pez , nombre_pez , tipo_agua) values
('6','Danio Cebra','Tropical')
returning
tipo_pez , nombre_pez , tipo_agua;
"""
cur.execute(sql)
conn.commit()



# Crear Datos Botia Payaso
sql = """
insert into rangos_peces (tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min) values
('7','6,5','6,0','30','25')
returning
tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min;
"""
cur.execute(sql)
conn.commit()
sql="""
insert into tipos_aceptados (tipo_pez , nombre_pez , tipo_agua) values
('7','Botia Payaso','Tropical')
returning
tipo_pez , nombre_pez , tipo_agua;
"""
cur.execute(sql)
conn.commit()


# Crear Datos Xipho
sql = """
insert into rangos_peces (tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min) values
('8','8,3','7,0','28','18')
returning
tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min;
"""
cur.execute(sql)
conn.commit()
sql="""
insert into tipos_aceptados (tipo_pez , nombre_pez , tipo_agua) values
('8','Xipho','Tropical')
returning
tipo_pez , nombre_pez , tipo_agua;
"""
cur.execute(sql)
conn.commit()


# Crear Datos Scalare
sql = """
insert into rangos_peces (tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min) values
('9','7,8','7,3','28','24')
returning
tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min;
"""
cur.execute(sql)
conn.commit()
sql="""
insert into tipos_aceptados (tipo_pez , nombre_pez , tipo_agua) values
('9','Scalare','Tropical')
returning
tipo_pez , nombre_pez , tipo_agua;
"""
cur.execute(sql)
conn.commit()


# Crear Datos Pangasius
sql = """
insert into rangos_peces (tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min) values
('10','7,2','6,8','26','22')
returning
tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min;
"""
cur.execute(sql)
conn.commit()
sql="""
insert into tipos_aceptados (tipo_pez , nombre_pez , tipo_agua) values
('10','Pangasius','Tropical')
returning
tipo_pez , nombre_pez , tipo_agua;
"""
cur.execute(sql)
conn.commit()


# Crear Datos Disco Azul Royal Blue
sql = """
insert into rangos_peces (tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min) values
('11','6,6','6,4','30','26')
returning
tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min;
"""
cur.execute(sql)
conn.commit()
sql="""
insert into tipos_aceptados (tipo_pez , nombre_pez , tipo_agua) values
('11','Disco Azul Royal Blue','Tropical')
returning
tipo_pez , nombre_pez , tipo_agua;
"""
cur.execute(sql)
conn.commit()


# Crear Datos Plecostomus Punteado
sql = """
insert into rangos_peces (tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min) values
('12','7,8','6,5','28','22')
returning
tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min;
"""
cur.execute(sql)
conn.commit()
sql="""
insert into tipos_aceptados (tipo_pez , nombre_pez , tipo_agua) values
('12','Plecostomus Punteado','Tropical')
returning
tipo_pez , nombre_pez , tipo_agua;
"""
cur.execute(sql)
conn.commit()

# Crear Datos Piraña roja
sql = """
insert into rangos_peces (tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min) values
('13','7,5','5,5','27','23')
returning
tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min;
"""
cur.execute(sql)
conn.commit()
sql="""
insert into tipos_aceptados (tipo_pez , nombre_pez , tipo_agua) values
('13','Piraña roja','Tropical')
returning
tipo_pez , nombre_pez , tipo_agua;
"""
cur.execute(sql)
conn.commit()


conn.close()
