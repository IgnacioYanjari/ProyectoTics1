from app import app
from datetime import datetime
from flask import render_template,request,redirect
from config import *
import psycopg2
import time
import serial

conn = psycopg2.connect("dbname=%s host=%s user=%s password=%s"%(database,host,user,password))
cur = conn.cursor()

@app.route('/')
@app.route('/index')
def index():
    #arduinoPort = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    #time.sleep(2)
    #getSerialValue=arduinoPort.readline()
    #print("Valor : ", getSerialValue)
    return render_template("index.html")
    #return render_template("index.html",temperatura=getSerialValue)
    #return render_template("index.html")
