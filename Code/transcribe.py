import whisper

def transcribe_audio(file_path):
    try:
        model = whisper.load_model("small")  # Oder "medium", "large"
        result = model.transcribe(file_path)
        
        if result and "text" in result:
            return result["text"]
        else:
            raise ValueError("Transkription fehlgeschlagen.")
    except Exception as e:
        print(f"Fehler bei der Transkription: {e}")
        return None

# Teste mit einer Beispiel-Audiodatei
transcription = transcribe_audio("C:/Users/Philipp/KI_tool/Programmentwurf-Anwendungen_von_Sprachmodellen/mp3_datei\DEUTSCHE_WIRTSCHAFT_Strompreis-Forderung_Industriekonferenz_mit_Habeck_sucht_Wege_aus_der_Krise_[_YouConvert.net_].mp3")
if transcription:
    print("Transkription erfolgreich:", transcription)
else:
    print("Transkription fehlgeschlagen.")
