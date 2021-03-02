from flask import Flask, url_for, send_from_directory
from flask import render_template, request
from app import Config

app = Flask(__name__)

@app.route("/")
def main_index():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/about")
def about():
    return render_template("about.html")

#заюзать позже
#@app.route("/<name>")
#def user(name):
#    return f"Hello {name}"



if __name__ == '__main__':
    app.config.from_object(Config)
    app.run()