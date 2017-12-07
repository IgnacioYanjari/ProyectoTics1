from config import *
from datetime import datetime
import psycopg2

conn = psycopg2.connect("dbname=%s host=%s user=%s password=%s"%(database,host,user,password))
cur = conn.cursor()

################################################################################

# Crear Datos de Peces Tropicales


# Crear Datos Esturión
sql = """
insert into rangos_peces (tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min) values
 ('1','7.6','7.4','18','10')
returning
tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min;
"""
cur.execute(sql)
conn.commit()

sql="""
insert into tipos_aceptados (tipo_pez , nombre_tipo , tipo_agua, litros_de_pez) values
('1','Esturión','Tropical','500')
returning
tipo_pez , nombre_tipo , tipo_agua;
"""
cur.execute(sql)
conn.commit()


# Crear Datos Cardenal
sql = """
insert into rangos_peces (tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min) values
('2','6.2','5.8','27','23')
returning
tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min;
"""
cur.execute(sql)
conn.commit()
sql="""
insert into tipos_aceptados (tipo_pez , nombre_tipo , tipo_agua, litros_de_pez) values
('2','Cardenal','Tropical','3')
returning
tipo_pez , nombre_tipo , tipo_agua;
"""
cur.execute(sql)
conn.commit()



# Crear Datos Monjita
sql = """
insert into rangos_peces (tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min) values
('3','8.5','5.8','26','20')
returning
tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min;
"""
cur.execute(sql)
conn.commit()
sql="""
insert into tipos_aceptados (tipo_pez , nombre_tipo , tipo_agua,litros_de_pez) values
('3','Monjita','Tropical','6')
returning
tipo_pez , nombre_tipo , tipo_agua;
"""
cur.execute(sql)
conn.commit()


# Crear Datos Tetra de cabeza roja
sql = """
insert into rangos_peces (tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min) values
('4','7.8','7.3','26','23')
returning
tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min;
"""
cur.execute(sql)
conn.commit()
sql="""
insert into tipos_aceptados (tipo_pez , nombre_tipo , tipo_agua,litros_de_pez) values
('4','Tetra de cabeza roja','Tropical','4')
returning
tipo_pez , nombre_tipo , tipo_agua;
"""
cur.execute(sql)
conn.commit()


# Crear Datos Barbo Tetrazona
sql = """
insert into rangos_peces (tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min) values
('5','7.0','6.0','26','20')
returning
tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min;
"""
cur.execute(sql)
conn.commit()
sql="""
insert into tipos_aceptados (tipo_pez , nombre_tipo , tipo_agua, litros_de_pez) values
('5','Barbo Tetrazona','Tropical', '7.5')
returning
tipo_pez , nombre_tipo , tipo_agua;
"""
cur.execute(sql)
conn.commit()


# Crear Datos Danio Cebra
sql = """
insert into rangos_peces (tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min) values
('6','7.0','6.5','24','18')
returning
tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min;
"""
cur.execute(sql)
conn.commit()
sql="""
insert into tipos_aceptados (tipo_pez , nombre_tipo , tipo_agua, litros_de_pez) values
('6','Danio Cebra','Tropical','6')
returning
tipo_pez , nombre_tipo , tipo_agua;
"""
cur.execute(sql)
conn.commit()



# Crear Datos Botia Payaso
sql = """
insert into rangos_peces (tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min) values
('7','6.5','6.0','30','25')
returning
tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min;
"""
cur.execute(sql)
conn.commit()
sql="""
insert into tipos_aceptados (tipo_pez , nombre_tipo , tipo_agua, litros_de_pez) values
('7','Botia Payaso','Tropical', '30')
returning
tipo_pez , nombre_tipo , tipo_agua;
"""
cur.execute(sql)
conn.commit()


# Crear Datos Xipho
sql = """
insert into rangos_peces (tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min) values
('8','8.3','7.0','28','18')
returning
tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min;
"""
cur.execute(sql)
conn.commit()
sql="""
insert into tipos_aceptados (tipo_pez , nombre_tipo , tipo_agua, litros_de_pez) values
('8','Xipho','Tropical', '30')
returning
tipo_pez , nombre_tipo , tipo_agua;
"""
cur.execute(sql)
conn.commit()


# Crear Datos Scalare
sql = """
insert into rangos_peces (tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min) values
('9','7.8','7.3','28','24')
returning
tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min;
"""
cur.execute(sql)
conn.commit()
sql="""
insert into tipos_aceptados (tipo_pez , nombre_tipo , tipo_agua, litros_de_pez) values
('9','Scalare','Tropical', '15')
returning
tipo_pez , nombre_tipo , tipo_agua;
"""
cur.execute(sql)
conn.commit()


# Crear Datos Pangasius
sql = """
insert into rangos_peces (tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min) values
('10','7.2','6.8','26','22')
returning
tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min;
"""
cur.execute(sql)
conn.commit()
sql="""
insert into tipos_aceptados (tipo_pez , nombre_tipo , tipo_agua, litros_de_pez) values
('10','Pangasius','Tropical','150')
returning
tipo_pez , nombre_tipo , tipo_agua;
"""
cur.execute(sql)
conn.commit()


# Crear Datos Disco Azul Royal Blue
sql = """
insert into rangos_peces (tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min) values
('11','6.6','6.4','30','26')
returning
tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min;
"""
cur.execute(sql)
conn.commit()
sql="""
insert into tipos_aceptados (tipo_pez , nombre_tipo , tipo_agua, litros_de_pez) values
('11','Disco Azul Royal Blue','Tropical', '10')
returning
tipo_pez , nombre_tipo , tipo_agua;
"""
cur.execute(sql)
conn.commit()


# Crear Datos Plecostomus Punteado
sql = """
insert into rangos_peces (tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min) values
('12','7.8','6.5','28','22')
returning
tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min;
"""
cur.execute(sql)
conn.commit()
sql="""
insert into tipos_aceptados (tipo_pez , nombre_tipo , tipo_agua, litros_de_pez) values
('12','Plecostomus Punteado','Tropical','50')
returning
tipo_pez , nombre_tipo , tipo_agua;
"""
cur.execute(sql)
conn.commit()

# Crear Datos Piraña roja
sql = """
insert into rangos_peces (tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min) values
('13','7.5','5.5','27','23')
returning
tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min;
"""
cur.execute(sql)
conn.commit()
sql="""
insert into tipos_aceptados (tipo_pez , nombre_tipo , tipo_agua,litros_de_pez) values
('13','Piraña roja','Tropical','30')
returning
tipo_pez , nombre_tipo , tipo_agua;
"""
cur.execute(sql)
conn.commit()

################################################################################

# Insertar tipos de peces frios

# Crear Datos Shubunkin

sql = """
insert into rangos_peces (tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min) values
('14','7.5','6.5','18','8')
returning
tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min;
"""
cur.execute(sql)
conn.commit()
sql="""
insert into tipos_aceptados (tipo_pez , nombre_tipo , tipo_agua,litros_de_pez) values
('14','Shubunkin','Agua fria','15')
returning
tipo_pez , nombre_tipo , tipo_agua;
"""
cur.execute(sql)
conn.commit()


# Crear Datos Carpa común
sql = """
insert into rangos_peces (tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min) values
('15','7.5','7','23','10')
returning
tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min;
"""
cur.execute(sql)
conn.commit()
sql="""
insert into tipos_aceptados (tipo_pez , nombre_tipo , tipo_agua, litros_de_pez) values
('15','Carpa común','Agua fria','50')
returning
tipo_pez , nombre_tipo , tipo_agua;
"""
cur.execute(sql)
conn.commit()

#Crear Datos Telescopio
sql = """
insert into rangos_peces (tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min) values
('16','7.5','7','23','18')
returning
tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min;
"""
cur.execute(sql)
conn.commit()
sql="""
insert into tipos_aceptados (tipo_pez , nombre_tipo , tipo_agua,litros_de_pez) values
('16','Telescopio','Agua fria','8')
returning
tipo_pez , nombre_tipo , tipo_agua;
"""
cur.execute(sql)
conn.commit()

#Crear Datos Burbuja
sql = """
insert into rangos_peces (tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min) values
('17','7.5','6.5','23','21')
returning
tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min;
"""
cur.execute(sql)
conn.commit()
sql="""
insert into tipos_aceptados (tipo_pez , nombre_tipo , tipo_agua,litros_de_pez) values
('17','Burbuja','Agua fria','13')
returning
tipo_pez , nombre_tipo , tipo_agua;
"""
cur.execute(sql)
conn.commit()

#Crear Datos Cabeza de León
sql = """
insert into rangos_peces (tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min) values
('18','7.5','6.5','21','8')
returning
tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min;
"""
cur.execute(sql)
conn.commit()
sql="""
insert into tipos_aceptados (tipo_pez , nombre_tipo , tipo_agua,litros_de_pez) values
('18','Cabeza de León','Agua fria','21')
returning
tipo_pez , nombre_tipo , tipo_agua;
"""
cur.execute(sql)
conn.commit()

#Crear Datos Cabeza de León holandés
sql = """
insert into rangos_peces (tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min) values
('19','7.5','6.5','22','18')
returning
tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min;
"""
cur.execute(sql)
conn.commit()
sql="""
insert into tipos_aceptados (tipo_pez , nombre_tipo , tipo_agua,litros_de_pez) values
('19','Cabeza de León holandés','Agua fria','20')
returning
tipo_pez , nombre_tipo , tipo_agua;
"""
cur.execute(sql)
conn.commit()

#Crear Datos Calico Fantail
sql = """
insert into rangos_peces (tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min) values
('20','7.5','6.5','22','18')
returning
tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min;
"""
cur.execute(sql)
conn.commit()
sql="""
insert into tipos_aceptados (tipo_pez , nombre_tipo , tipo_agua, litros_de_pez) values
('20','Calico Fantail','Agua fria','15')
returning
tipo_pez , nombre_tipo , tipo_agua;
"""
cur.execute(sql)
conn.commit()

#Crear Datos Carpa
sql = """
insert into rangos_peces (tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min) values
('21','8.5','6','32','0')
returning
tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min;
"""
cur.execute(sql)
conn.commit()
sql="""
insert into tipos_aceptados (tipo_pez , nombre_tipo , tipo_agua,litros_de_pez) values
('21','Carpa','Agua fria','120')
returning
tipo_pez , nombre_tipo , tipo_agua;
"""
cur.execute(sql)
conn.commit()

#Crear Datos Celestial
sql = """
insert into rangos_peces (tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min) values
('22','7.5','6.5','21','16')
returning
tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min;
"""
cur.execute(sql)
conn.commit()
sql="""
insert into tipos_aceptados (tipo_pez , nombre_tipo , tipo_agua,litros_de_pez) values
('22','Celestial','Agua fria','13')
returning
tipo_pez , nombre_tipo , tipo_agua;
"""
cur.execute(sql)
conn.commit()

#Crear Datos Fantail
sql = """
insert into rangos_peces (tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min) values
('23','7.5','6.5','20','8')
returning
tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min;
"""
cur.execute(sql)
conn.commit()
sql="""
insert into tipos_aceptados (tipo_pez , nombre_tipo , tipo_agua,litros_de_pez) values
('23','Fantail','Agua fria','15')
returning
tipo_pez , nombre_tipo , tipo_agua;
"""
cur.execute(sql)
conn.commit()


#Crear Datos Goldfish
sql = """
insert into rangos_peces (tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min) values
('24','7.5','6.5','22','18')
returning
tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min;
"""
cur.execute(sql)
conn.commit()
sql="""
insert into tipos_aceptados (tipo_pez , nombre_tipo , tipo_agua,litros_de_pez) values
('24','Goldfish','Agua fria','20')
returning
tipo_pez , nombre_tipo , tipo_agua;
"""
cur.execute(sql)
conn.commit()

#Crear Datos Jikin
sql = """
insert into rangos_peces (tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min) values
('25','7.5','6.5','22','18')
returning
tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min;
"""
cur.execute(sql)
conn.commit()
sql="""
insert into tipos_aceptados (tipo_pez , nombre_tipo , tipo_agua,litros_de_pez) values
('25','Jikin','Agua fria','12')
returning
tipo_pez , nombre_tipo , tipo_agua;
"""
cur.execute(sql)
conn.commit()

#Crear Datos Shubunkin London
sql = """
insert into rangos_peces (tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min) values
('26','7.5','6.5','20','0')
returning
tipo_pez, ph_max, ph_min , temperatura_max ,temperatura_min;
"""
cur.execute(sql)
conn.commit()
sql="""
insert into tipos_aceptados (tipo_pez , nombre_tipo , tipo_agua,litros_de_pez) values
('26','Shubunkin London','Agua fria','12')
returning
tipo_pez , nombre_tipo , tipo_agua;
"""
cur.execute(sql)
conn.commit()

#Iniciamos la pecera
sql="""
insert into peceras(id,nombre,galones,litros,litros_disponibles) values
('1','Pecera1','2.49','9.45','9.45')
"""
cur.execute(sql)
conn.commit()


conn.close()
