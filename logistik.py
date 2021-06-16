import sqlite3
import flask
from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/url.main")
def project():
    return render_template("project.html")

@app.route("/url.login")
def log():
    return render_template("login.html")

@app.route("/url.register")
def reg():
    return render_template("reg.html")

@app.route("/addblog")
def addblog():
    return render_template("create.html", methods=['POST'])

app.run()