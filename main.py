from flask import Flask, render_template
import requests
import csv
import io

app = Flask(__name__)

@app.route("/")
def hello_world():
    records = get_records()
    return render_template("home.html", records=records)

def get_records():

    f = open("CSV.const", "r")

    URL = f.read()

    response = requests.get(URL)
    response.raise_for_status()
    
    content = io.StringIO(response.text)
    reader = csv.DictReader(content)

    return list(reader)