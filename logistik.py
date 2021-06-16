import sqlite3
import flask
from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/")
def project():
    return render_template("project.html")

@app.route("/")
def log():
    return render_template("login.html")

@app.route("/")
def reg():
    return render_template("reg.html")

@app.route("/")
def blog():
    return render_template("create.html")

app.run()