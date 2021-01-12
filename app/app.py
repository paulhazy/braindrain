from flask import Flask
from config import Config

app = Flask(__name__)
#get configuration from config.py class Config
app.config.from_object(Config)