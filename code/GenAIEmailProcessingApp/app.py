import os
from apiflask import APIFlask
from flask import Flask, render_template, request, jsonify
from util.email_classification import summarize_eml_file
from flask_bootstrap import Bootstrap5
import json

app = APIFlask(__name__)
# Define the upload folder
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create the upload folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

Bootstrap5(app)

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
            # Get the filename
            filename = file.filename
            # Construct the full filepath
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            # Save the file
            file.save(filepath)
        
            summary = summarize_eml_file(filepath)
            summary = summary.replace("```json", "").replace("```", "")  # Remove JSON formatting
            print(summary)
        else:
            summary = None
        
        response = {
            "message": "File uploaded and parameters received",
            "file_name": file.filename if file else None,
            "param1": param1,
            "param2": param2,
            "results": json.loads(summary)  # Convert summary to JSON object
        }
        return jsonify(response)
    return render_template("upload.html")