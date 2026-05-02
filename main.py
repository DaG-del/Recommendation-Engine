from flask import Flask, Blueprint, render_template, request, redirect, url_for, session, current_app

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)

@auth.route("/")
def hello_world():
    return render_template("hello_world.html")