from flask import Flask, render_template, request
from PIL import Image
from time import sleep
import json
import random

app = Flask("app")

@app.route("/")
def hello_world():
	return render_template("index.html")


@app.route("/survey")
def survey():
	return render_template("survey.js")


@app.route("/model_code")
def model_code_nb():
	return render_template("model_notebook.html")


@app.route('/results')
def results():
	return f"<h1>It Works!</h1>"

app.run(host="0.0.0.0", port=8080, debug=True)
