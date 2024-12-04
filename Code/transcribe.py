import whisper  # Das Whisper-Modul wird importiert. Whisper ist ein OpenAI-Modell zur automatischen Spracherkennung (ASR).

def transcribe_audio(file_path):
    # Eine Funktion wird definiert, die eine Audiodatei transkribiert.
    # `file_path` ist der Pfad zur Eingabedatei, die transkribiert werden soll.

    model = whisper.load_model("base")
    # Hier wird das Whisper-Modell geladen. "base" bezeichnet ein vortrainiertes Modell in mittlerer Größe.
    # Es gibt auch andere Modellgrößen, wie "tiny", "small", "medium", "large", die unterschiedliche Genauigkeit und Rechenleistung erfordern.

    result = model.transcribe(file_path)
    # Die Funktion `transcribe` des geladenen Modells wird aufgerufen.
    # Sie verarbeitet die Audiodatei, die unter `file_path` gespeichert ist, und gibt ein Ergebnis-Objekt zurück.
    # Dieses Objekt enthält mehrere Informationen, einschließlich der transkribierten Texte.

    return result["text"]
    # Der transkribierte Text wird aus dem Ergebnis-Objekt extrahiert und zurückgegeben.
    # `result["text"]` enthält die reine Texttranskription der Audiodatei.

# Beispiel-Nutzung:
# text = transcribe_audio("audio.mp3")
# print(text)
