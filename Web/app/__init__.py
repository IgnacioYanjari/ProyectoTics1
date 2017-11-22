from flask import Flask,jsonify

app = Flask(__name__,template_folder='template')
from app import views
