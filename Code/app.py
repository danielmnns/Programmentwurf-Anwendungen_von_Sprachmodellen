from flask import Flask, render_template, request, jsonify
from transcribe import transcribe_audio
from summarize import summarize_text

app = Flask(__name__)

# Route für die Hauptseite (Frontend)
@app.route('/')
def index():
    return render_template('index.html')  # Stelle sicher, dass index.html existiert

# Route für die API-Verarbeitung
@app.route('/api/process', methods=['POST'])
def process():
    # Überprüfen, ob eine Datei hochgeladen wurde
    if 'audio_file' not in request.files:
        return jsonify({"error": "Keine Datei hochgeladen"}), 400
    
    audio_file = request.files['audio_file']
    
    # Speichern der Datei im temporären Ordner
    file_path = f"./uploads/{audio_file.filename}"
    audio_file.save(file_path)
    
    try:
        # Transkription der Audiodatei
        transcription = transcribe_audio(file_path)
        
        # Zusammenfassung des Transkripts
        summary = summarize_text(transcription)
        
        # Rückgabe der Ergebnisse an das Frontend
        return jsonify({
            "transcription": transcription,
            "summary": summary
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
