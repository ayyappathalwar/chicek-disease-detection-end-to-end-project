from flask import Flask, jsonify, request, render_template
import os
from flask_cors import CORS, cross_origin
from cnnClassifier.utils.common import decodeImage



os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')


app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(filename=self.filename)


@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template("index.html")


@app.route("/", methods=["GET", "POST"])
@cross_origin()
def trainRoute():
    os.system("python main.py")
    return "Training done successfully"
