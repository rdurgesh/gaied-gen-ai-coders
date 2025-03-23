from flask import Flask, render_template, request, jsonify
from util.email_classification import summarize_eml_file
from flask_bootstrap import Bootstrap
import json

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process_email", methods=["POST"])
def process_email():
    if request.method == "POST":
        file = request.files.get("file")
        param1 = request.form.get("param1")
        param2 = request.form.get("param2")
        # Process the file and parameters here
        if file:
            summary = summarize_eml_file(file)
            summary = summary.replace("```json", "").replace("```", "")  # Remove JSON formatting
            print(summary)
        else:
            summary = None
        
        response = {
            "message": "File uploaded and parameters received",
            "file_name": file.filename if file else None,
            "param1": param1,
            "param2": param2,
            "summary": json.loads(summary)  # Convert summary to JSON object
        }
        return jsonify(response)
    return render_template("upload.html")