1. Requerimientos software:

	- Flask
	- Postgresql 
	- Python3
	- Libreria psycopg2 (Python3 se instala con pip3)

2. Pasos para uso de software: 
	
	- Crear usuario tics en postgresql
	- Crear bdd tics en postgresql
	- Asignar permisos de tics sobre la bdd creada
	- Ejecutar el archivo setup.py con python3 (Configuración de tablas) :
		```bash
		python3 setup.py
		```		
	- Ejecutar el archivo seed.py con python3 (Inicialización de valores predeterminados):
		```python
		python3 seed.py def: Structure1
		```		
	- Levantar el servidor con permisos de administrador (Debido a que utiliza el puerto 80)  con sudo en ubuntu por ejemplo ejecutando el archivo run.py con python3.py:
		```bash
		sudo python3 run.py
		```		
	- Abrir página en cualquier navegador con las ruta localhost o 0.0.0.0
	- Visualización de la Página Web
	![Imagen predefinida de la Pagina](https://github.com/IgnacioYanjari/ProyectoTics1/blob/master/Imagenes/Pagina_Web.png)
	
