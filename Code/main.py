from flask import Flask, render_template, request, jsonify
from transcribe import transcribe_audio
from summarize import summarize_text
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Verzeichnis zum Speichern der Audiodateien
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Route für die Hauptseite (Frontend)
@app.route('/')
def index():
    return render_template('index.html')  # Dein Frontend HTML

# Route für die API-Verarbeitung
@app.route('/api/process', methods=['POST'])
def process():
    if 'audio_file' not in request.files:
        return jsonify({"error": "Keine Datei hochgeladen"}), 400
    
    audio_file = request.files['audio_file']
    
    # Sicherstellen, dass der Dateiname sicher ist
    filename = secure_filename(audio_file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    # Speichern der Audioaufnahme
    audio_file.save(file_path)
    
    try:
        # Transkription der Audiodatei
        transcription = transcribe_audio(file_path)
        
        # Zusammenfassung mit Ollama (Llama 3.2)
        summary = summarize_text(transcription)
        
        return jsonify({
            "transcription": transcription,
            "summary": summary
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
