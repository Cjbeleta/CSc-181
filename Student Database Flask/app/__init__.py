from flask import Flask
from model import *

app = Flask(__name__)
app.static_folder = 'static'

from app import controller