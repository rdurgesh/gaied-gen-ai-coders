from flask import Flask, render_template, request, jsonify
from util.email_classification import summarize_eml_file

app = Flask(__name__)

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
        else:
            summary = None
        response = {
            "message": "File uploaded and parameters received",
            "file_name": file.filename if file else None,
            "param1": param1,
            "param2": param2,
            "summary": summary
        }
        return jsonify(response)
    return render_template("upload.html")