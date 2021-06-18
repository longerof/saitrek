import sqlite3
<<<<<<< HEAD
import flask
from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/")
def project():
    return render_template("project.html")

@app.route("/login")
def log():
    return render_template("login.html")

@app.route("/register")
def reg():
    return render_template("reg.html")

@app.route("/addblog")
def addblog():
    return render_template("create.html", methods=['POST'])
=======
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("project.html")

@app.route('/reg')
def reg():
    return render_template("reg.html")

@app.route('/reg/fun', methods=['POST'])
def reg_fun():
    family = request.form["family"]
    email = request.form["email"]
    psw = request.form["psw"]
    connect = sqlite3.connect("database.db")
    cursor = connect.cursor()

    cursor.execute("INSERT INTO users (family, email, psw) VALUES (?, ?, ?)", (family, email, psw))
    connect.commit()
    return redirect("/")

@app.route('/log')
def log():
    return render_template("login.html")

@app.route('/log/fun')
def log_fun():
    return ""

@app.route('/cre')
def cre():
    return render_template("create.html")

@app.route('/cre/fun')
def cre_fun():
    return ""

@
>>>>>>> 023607882e950ee320e067f595d0332806183265

app.run()