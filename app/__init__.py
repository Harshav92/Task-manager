from flask import Flask
from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:Prjreddy_64@localhost/tasks"

db = SQLAlchemy(app)
migrate = Migrate(app,db)


