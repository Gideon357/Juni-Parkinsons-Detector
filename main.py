from flask import Flask, render_template, request
import json

app = Flask("app")


@app.route("/")
def hello_world():
	if request.user_agent.browser == "msie":
		return render_template("html/msie.html")
	else:
		return render_template("html/index.html")


@app.route("/survey")
def survey():
	return render_template("js/survey.js")


@app.route("/model_code")
def model_code_nb():
	return render_template("html/model_notebook.html")


@app.route('/results')
def results():
	raw_result = request.args.get('results')
	result = json.loads(raw_result)
	return result

app.run(host="0.0.0.0", port=8080, debug=True)
