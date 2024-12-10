from flask import Flask, request, jsonify, render_template
import os
from werkzeug.utils import secure_filename
import base64
from transcribe import transcribe_audio
from summarize import summarize_text

# Erstelle eine Flask-App-Instanz
app = Flask(__name__)

# Konfiguriere den Upload-Ordner und maximale Dateigröße
app.config['UPLOAD_FOLDER'] = 'uploads'  # Ordner für hochgeladene Dateien
app.config['MAX_CONTENT_LENGTH'] = 32 * 1024 * 1024  # Maximale Dateigröße von 32 MB

@app.route('/')
def index():
    # Route für die Startseite der Anwendung; gibt eine HTML-Vorlage zurück
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    # Route zum Hochladen und Verarbeiten von Audiodateien
    if 'audio-file' in request.files:  
        # Überprüfung, ob eine Datei hochgeladen wurde
        audio_file = request.files['audio-file']  # Zugriff auf die hochgeladene Datei
        filename = secure_filename(audio_file.filename)  # Sichere den Dateinamen
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)  # Bestimme den Pfad
        audio_file.save(file_path)  # Speichere die Datei auf dem Server
    elif 'recorded-audio' in request.form:
        # Verarbeitung von Audio-Daten, die direkt vom Benutzer aufgezeichnet wurden
        audio_data = request.form['recorded-audio'].split(",")[1]  # Extrahiere den Base64-kodierten Inhalt
        filename = "recorded_audio.wav"  # Definiere einen Standardnamen für die Aufnahme
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)  # Pfad zur Speicherung
        with open(file_path, "wb") as f:
            f.write(base64.b64decode(audio_data))  # Dekodiere und speichere die Audio-Daten
    else:
        # Wenn keine Datei bereitgestellt wird, sende eine Fehlermeldung
        return jsonify({"error": "No audio file provided"}), 400

    try:
        # Transkription der Audiodatei mit externer Funktion
        transcription = transcribe_audio(file_path)
        
        # Zusammenfassung der Transkription mit externer Funktion
        summary = summarize_text(transcription)
        
        # Rückgabe der Transkription und der Zusammenfassung im JSON-Format
        return jsonify({
            "transcription": transcription,
            "summary": summary
        })
    except Exception as e:
        # Fehlerbehandlung bei der Verarbeitung
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Starte die Anwendung im Debug-Modus
    app.run(debug=True)
