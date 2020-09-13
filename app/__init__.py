from flask import Flask
from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy 
from .route import todo
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:Prjreddy_64@localhost/tasks"
app.register_blueprint(todo, url_prefix="")
db = SQLAlchemy(app)



