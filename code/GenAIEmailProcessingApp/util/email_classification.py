import os
import json
from google import genai

def summarize_eml_file(uploaded_file):
    print("Starting to summarize the email file.")
    content = uploaded_file.read().decode()
    print("Email content extracted.")

    # Load request types for classification
    with open(os.path.join(os.path.dirname(__file__), '..', 'input', 'requestTypes.json'), 'r') as f:
        request_types = json.load(f)
    print("Loaded request types for classification.")

    api_key = os.environ.get("GENAI_API_KEY") or os.getenv("GENAI_API_KEY")
    print(f"Retrieved API key: {api_key}")  # Debug print statement
    if api_key is None:
        raise ValueError("API key is not set. Please set the GENAI_API_KEY environment variable.")
    
    client = genai.Client(api_key=api_key)
    print("GenAI client initialized.")
    response = client.models.generate_content(
        model="gemini-2.0-flash", 
        contents=f"summarize, classify based on the following request types {request_types} & its confidence score, extract key fields & return it in json format : {content}"
    )
    print("Received response from GenAI.")
    return response.text

def process_sample_folder():
    sample_folder = 'D:\\git\\gaied-gen-ai-coders\\code\\GenAIEmailProcessingApp\\samples'
    print(f"Processing sample folder: {sample_folder}")
    for filename in os.listdir(sample_folder):
        if filename.endswith('.txt'):
            file_path = os.path.join(sample_folder, filename)
            print(f"Processing file: {file_path}")
            with open(file_path, 'rb') as file:
                summary = summarize_eml_file(file)
                print(f"Summary for {filename}:\n{summary}\n")
            break

# Example usage
# with open('d:\\git\\gaied-gen-ai-coders\\code\\test_email.eml', 'rb') as file:
#     summary = summarize_eml_file(file)
#     print(summary)

# Example usage
#process_sample_folder()
