from app import app
#app.config['SERVER_NAME'] = 'myapp.dev'
#app.config['SERVER_NAME']='myapp.dev'
app.run(host='0.0.0.0',port=80,debug=True)
#app.run(threaded=True)
#port=80
#app.run(host= '0.0.0.0')# to run on your machines IP address.

#from tornado.wsgi import WSGIContainer
#from tornado.httpserver import HTTPServer
#from tornado.ioloop import IOLoop
#from app import app

#http_server = HTTPServer(WSGIContainer(app))
#http_server.listen(5000)
#IOLoop.instance().start()
