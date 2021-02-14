from flask import Flask, url_for
from flask import render_template, request
from app import app

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

#заюзать позже
#@app.route("/<name>")
#def user(name):
#    return f"Hello {name}"

if __name__ == '__main__':
    app.run()


