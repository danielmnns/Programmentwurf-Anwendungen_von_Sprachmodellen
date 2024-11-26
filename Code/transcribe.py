import whisper

def transcribe_audio(file_path):
    model = whisper.load_model("base")  # Oder "small", "medium", "large"
    result = model.transcribe(file_path)
    return result["text"]

if __name__ == "__main__":
    transcription = transcribe_audio("meeting_audio.mp3")
    print(transcription)
