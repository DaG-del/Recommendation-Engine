from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    records = []
    return render_template("home.html", records=records)