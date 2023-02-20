from flask import Flask, render_template 

app = Flask(__name__)

@app.route("/index")
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/style")
def style():
    return render_template("style.css")

