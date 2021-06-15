import sqlite3
import flask
from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/")
def project():
    return render_template("project.html")

app.run()