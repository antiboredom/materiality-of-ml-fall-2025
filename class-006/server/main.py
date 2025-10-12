from flask import Flask, request, render_template, jsonify
from transformers import pipeline
from PIL import Image
import io

app = Flask(__name__)

classifier = pipeline("image-classification", model="google/vit-base-patch16-224")

text_classifier = pipeline("sentiment-analysis")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/text")
def text():
    return render_template("text_classification.html")


@app.route("/classify_image", methods=["POST"])
def classify_image():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    try:
        # Read and process the image
        image_bytes = file.read()
        image = Image.open(io.BytesIO(image_bytes))

        # Convert to RGB if necessary
        if image.mode != "RGB":
            image = image.convert("RGB")

        # Classify the image
        predictions = classifier(image)

        return jsonify({"predictions": predictions})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/classify_text", methods=["POST"])
def classify_text():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "No text provided"}), 400

    text = data["text"].strip()

    if not text:
        return jsonify({"error": "Text cannot be empty"}), 400

    try:
        # Classify the text
        result = text_classifier(text)
        return jsonify({"prediction": result[0]})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
