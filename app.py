from flask import Flask, render_template, request, send_file
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_audio', methods=['POST'])
def generate_audio():
    texts = request.form.getlist('text')
    files = []
    for i, text in enumerate(texts):
        tts = gTTS(text=text, lang='fr')  # 'fr' pour la langue française, changez selon vos besoins
        file_name = f"output_{i}.mp3"
        tts.save(file_name)
        files.append(file_name)
    return render_template('download.html', files=files)

@app.route('/download/<path:filename>')
def download(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
