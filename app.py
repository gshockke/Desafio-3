from flask import Flask, render_template
# from flask_bootstrap import Bootstrap
# from flask_mysqldb import MySql


app = Flask("__name__")


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/quem_somos")
def quem_somos():
    return render_template('quem_somos.html')

@app.route("/contato")
def contato():
    return render_template('contato.html')