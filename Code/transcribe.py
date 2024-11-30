import os
import warnings
import whisper

# Unterdrücken von FutureWarnings und UserWarnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)

# Dynamischer Pfad zur Audiodatei basierend auf dem aktuellen Arbeitsverzeichnis
current_dir = os.getcwd()
local_fp = os.path.join(current_dir, 'mp3_datei', 'test_audio.wav')

device = 'cpu'  # oder 'cuda', wenn GPU verwendet wird

# Ausgabe des Pfads zur Überprüfung
print(f"Pfad zur Audiodatei: {local_fp}")

# Überprüfen, ob die Datei existiert
if os.path.exists(local_fp):
    print("Die Datei existiert.")
    
    # Überprüfen der Dateiberechtigungen
    if os.access(local_fp, os.R_OK):
        print("Die Datei ist lesbar.")
        
        # Laden des Whisper-Modells
        model = whisper.load_model("base", device=device)
        
        # Transkription der Audiodatei
        try:
            result = model.transcribe(local_fp)
            # Ausgabe der Transkription
            print(result["text"])
        except Exception as e:
            print(f"Fehler bei der Transkription: {e}")
    else:
        print("Die Datei ist nicht lesbar. Überprüfen Sie die Berechtigungen.")
else:
    print(f"Fehler: Die Datei {local_fp} existiert nicht.")
    print("Überprüfen Sie den Pfad und stellen Sie sicher, dass die Datei vorhanden ist.")

# FP16-Warnung behandeln
if device == 'cpu':
    warnings.warn("FP16 wird auf der CPU nicht unterstützt; FP32 wird stattdessen verwendet")