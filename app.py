  GNU nano 8.1                                                    app.py                                                               
import logging
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from datetime import datetime
from flask_migrate import Migrate

# Initialize Flask application and database


def initialize_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://grocery_user:1234@localhost/grocery_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'parames@123'
    
    db.init_app(app)
    Migrate(app, db)
    return app
