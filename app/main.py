from flask import Flask, url_for
from flask import render_template, request


app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html", name=request.args.get("name"))

@app.route("/login")
def login():
    return render_template("login.html", login=request.args.get("login"))

@app.route("/<name>")
def user(name):
    return f"Hello {name}"



