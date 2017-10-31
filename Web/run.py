from app import app
#app.config['SERVER_NAME'] = 'myapp.dev'
#app.config['SERVER_NAME']='myapp.dev'
app.run(host='0.0.0.0',port=80,debug=True,threaded=True)
#app.run(threaded=True)
#port=80
#app.run(host= '0.0.0.0')# to run on your machines IP address.
