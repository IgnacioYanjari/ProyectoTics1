1. Requerimientos software:

	- Flask
	- Postgresql 
	- Python3
	- Libreria psycopg2 (Python3 se instala con pip3)

2. Pasos para uso de software: 
	
	- Crear usuario tics en postgresql
	- Crear bdd tics en postgresql
	- Asignar permisos de tics sobre la bdd creada
	- Ejecutar el archivo setup.py con python3 (Configuración de tablas)
	- Ejecutar el archivo seed.py con python3 (Inicialización de valores predeterminados)
	- Levantar el servidor con permisos de administrador (Debido a que utiliza el puerto 80)  con sudo en ubuntu por ejemplo.
	- Abrir página en cualquier navegador con las ruta localhost o 0.0.0.0
```c++
python app.py
```
