import os
import warnings
import whisper


# Relativer Pfad zur Audiodatei
local_fp = os.path.join(os.getcwd(), 'mp3_datei', 'test_audio2.mp3')

device = 'cpu'  # oder 'cuda', wenn GPU verwendet wird

# Ausgabe des Pfads zur Überprüfung
print(f"Pfad zur Audiodatei: {local_fp}")

# Überprüfen, ob die Datei existiert
if os.path.exists(local_fp):
    print("Die Datei existiert.")
    
    # Überprüfen der Dateiberechtigungen
    if os.access(local_fp, os.R_OK):
        print("Die Datei ist lesbar.")
        
        # Testen, ob die Datei direkt geöffnet werden kann
        try:
            with open(local_fp, 'rb') as f:
                print("Die Datei wurde erfolgreich geöffnet.")
        except Exception as e:
            print(f"Fehler beim Öffnen der Datei: {e}")
        
        # Laden des Whisper-Modells
        model = whisper.load_model("base", device=device)
        
        # Sprach-zu-Text-Transkription der Audiodatei
        try:
            print(f"Starte Sprach-zu-Text-Transkription der Datei: {local_fp}")
            result = model.transcribe(local_fp)
            # Ausgabe der Transkription
            print(result["text"])
        except Exception as e:
            print(f"Fehler bei der Sprach-zu-Text-Transkription: {e}")
    else:
        print("Die Datei ist nicht lesbar. Überprüfen Sie die Berechtigungen.")
else:
    print(f"Fehler: Die Datei {local_fp} existiert nicht.")
    print("Überprüfen Sie den Pfad und stellen Sie sicher, dass die Datei vorhanden ist.")

# FP16-Warnung behandeln
if device == 'cpu':
    warnings.warn("FP16 wird auf der CPU nicht unterstützt; FP32 wird stattdessen verwendet")