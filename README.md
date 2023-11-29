# Rodior
## Author🎙️...
- Wharkly47

## Description
Rodior is a Flask-based application that converts text into audio files using the Google Text-to-Speech (gTTS) library.

## Getting Started
### Prerequisites
- Python 3.x
- Flask
- gTTS library

### Installation
1. Clone the repository: `git clone https://github.com/Wharkly47/Rodior.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python3 app.py`

## Usage
1. Access the application through your browser at `http://localhost:5000`.
2. Enter the text you want to convert to audio in the input field.
3. Click the "Generate Audio" button.
4. Download the generated audio files.

## Files Structure
- `app.py`: Contains the Flask application routes.
- `templates/index.html`: HTML template for the user interface.
- `templates/download.html`: HTML template for downloading audio files.
- `output_*.mp3`: Generated audio files are saved here.

## Code Example
```python
from flask import Flask, render_template, request, send_file
from gtts import gTTS
import os

app = Flask(__name__)

# ... (Your Flask routes and functions)
Contact Information
Email: Wharklya@gmail.com
Feel free to reach out for any questions or inquiries!
