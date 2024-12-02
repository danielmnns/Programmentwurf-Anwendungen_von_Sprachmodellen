from flask import Flask, request, jsonify, render_template
import os
from werkzeug.utils import secure_filename
import base64
from transcribe import transcribe_audio
from summarize import summarize_text

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 32 * 1024 * 1024  # 32 MB


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'audio-file' in request.files:
        audio_file = request.files['audio-file']
        filename = secure_filename(audio_file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        audio_file.save(file_path)
    elif 'recorded-audio' in request.form:
        audio_data = request.form['recorded-audio'].split(",")[1]
        filename = "recorded_audio.wav"
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        with open(file_path, "wb") as f:
            f.write(base64.b64decode(audio_data))
    else:
        return jsonify({"error": "No audio file provided"}), 400

    try:
        # Transkription der Audiodatei
        transcription = transcribe_audio(file_path)
        
        # Zusammenfassung
        summary = summarize_text(transcription)
        
        return jsonify({
            "transcription": transcription,
            "summary": summary
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)