# GenAIEmailProcessingApp

## Overview
GenAIEmailProcessingApp is a Flask-based web application that processes email files and extracts summaries using a machine learning model.

## Features
- Upload email files in `.eml` or `.txt` or `.pdf` or `.docx` format.
- Extract and summarize the content of the email.
- Receive additional parameters for processing.

## Prerequisites
1. Get Gemini API Key:
   - Sign up at the Gemini API website and obtain your API key.
2. Set environment variable with name `GENAI_API_KEY` in Windows:
   

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/GenAIEmailProcessingApp.git
    ```
2. Navigate to the project directory:
    ```bash
    cd GenAIEmailProcessingApp
    py -3 -m venv .venv
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Start the Flask application:
    ```bash

    .venv\Scripts\activate
    flask run
    ```
2. Open your web browser and go to `http://127.0.0.1:5000/`.

## API Endpoints
### `GET /`
- Renders the main page.

### `POST /process_email`
- Processes the uploaded email file and additional parameters.
- **Request Parameters:**
  - `file`: The email file to be processed.
  - `param1`: Additional parameter 1.
  - `param2`: Additional parameter 2.
- **Response:**
  - `message`: Confirmation message.
  - `file_name`: Name of the uploaded file.
  - `param1`: Value of additional parameter 1.
  - `param2`: Value of additional parameter 2.
  - `summary`: Extracted summary of the email content.

## License
This project is licensed under the MIT License.
