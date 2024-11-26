import whisper

def transcribe_audio(file_path):
    model = whisper.load_model("base")  # Oder "small", "medium", "large"
    result = model.transcribe(file_path)
    return result["text"]
