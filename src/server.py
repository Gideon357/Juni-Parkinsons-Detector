# Standard imports
import uuid
import os

# Flask imports
from flask import Flask, request, jsonify, render_template, flash, redirect
from flask_cors import CORS
from werkzeug.utils import secure_filename

# FastAI imports
from fastai.basic_train import load_learner
from fastai.vision import open_image

# Constants
UPLOAD_FOLDER = "./uploads/"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

# Setup Flask
app = Flask(__name__)
CORS(app, support_credentials=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

upload_filename = None


def allowed_file(filename: str) -> str:
    """Checks for allowed file types"""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# Load the learner
learn = load_learner(path="./model/output/", file="final-model.pkl")
classes = learn.data.classes


def predict_single(img_file: str) -> dict:
    """function to take image and return prediction"""
    prediction = learn.predict(open_image(img_file))
    probs_list = prediction[2].numpy()
    return {
        "category": classes[prediction[1].item()],
        "probs": {c: round(float(probs_list[i]), 5) for (i, c) in enumerate(classes)},
    }


@app.route("/")
@app.route("/index")
@app.route("/form")
def form():
    return render_template("form.html")


@app.route("/process", methods=["GET", "POST"])
def process():
    global upload_filename
    if request.method == "POST":
        # check if the post request has the file part
        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)
        file = request.files["file"]
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            upload_filename = secure_filename(str(uuid.uuid4().hex))
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], str(uuid.uuid4().hex)))
    prediction = predict_single(
        os.path.join(app.config["UPLOAD_FOLDER"], str(uuid.uuid4().hex))
    )
    return None


@app.route("/api/predict", methods=["POST"])
def predict():
    """A JSON endpoint to for running inference"""
    return jsonify(predict_single(request.files["image"]))


if __name__ == "__main__":
    app.run()
