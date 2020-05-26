from flask import Flask, render_template
# from PIL import Image
# import json
# import pandas as pd

app = Flask("app")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/model_code")
def model_code_nb():
    return render_template("model_notebook.html")


@app.route("/results")
def results():
    return "<h1>It Works!</h1>"


app.run(host="0.0.0.0", port=8080, debug=True)
