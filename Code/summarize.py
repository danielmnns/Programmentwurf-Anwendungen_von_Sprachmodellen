import requests  # Modul für HTTP-Anfragen
import json  # Modul für die Verarbeitung von JSON-Daten
from langdetect import detect  # Modul zur Erkennung der Sprache eines Textes

def summarize_text(text):
    # Detectiert die Sprache des Textes
    language = detect(text)
    
    # Je nach erkannter Sprache wird die Zusammenfassungsanweisung angepasst
    if language == 'de':
        summary_instruction = 'Fasse die wesentlichen Informationen aus dem folgenden Text prägnant zusammen und erstelle eine Liste aller To-Dos.'  # Für Deutsch
    elif language == 'en':
        summary_instruction = 'Provide a concise summary of the key points in the following text and outline all the actionable to-dos.'  # Für Englisch
    else:
        # Standard-Anweisung für andere Sprachen
        summary_instruction = 'Fasse die wesentlichen Informationen aus dem folgenden Text prägnant zusammen und erstelle eine Liste aller To-Dos.'

    # API-Endpunkt der Ollama-Plattform (Lokaler Server mit Port 11434)
    url = "http://127.0.0.1:11434/api/chat"  

    # Payload mit den notwendigen Daten für die API-Anfrage
    payload = {
        'model': 'llama3.2',  # Das verwendete Modell
        'messages': [
            {'role': 'system', 'content': summary_instruction},  # Systemnachricht mit der Anweisung
            {'role': 'user', 'content': text}  # Der vom Benutzer eingegebene Text
        ],
        'stream': True  # Aktiviert das Streaming der Antwort
    }

    # Header für die Anfrage (Content-Type auf JSON gesetzt)
    headers = {'Content-Type': 'application/json'}
    
    # Senden der POST-Anfrage an die API
    response = requests.post(url, json=payload, headers=headers, stream=True)
    
    if response.status_code == 200:  # Überprüfen, ob die Antwort erfolgreich war
        full_content = ""  # Initialisierung der Variablen für den gesamten Inhalt der Antwort
        # Verarbeitung der Streaming-Daten (Zeile für Zeile)
        for line in response.iter_lines():
            if line:  # Wenn die Zeile nicht leer ist
                try:
                    fragment = json.loads(line)  # Versucht, die Zeile in JSON zu konvertieren
                    content_piece = fragment.get('message', {}).get('content', '')  # Extrahiert den Inhalt der Antwort
                    full_content += content_piece  # Fügt den Inhalt zum vollständigen Text hinzu
                except json.JSONDecodeError:
                    print("Fehler beim Dekodieren eines Fragments:", line)  # Fehlerbehandlung bei ungültigem JSON
        return full_content  # Gibt den vollständigen Inhalt der Antwort zurück
    else:
        # Falls die Anfrage fehlschlägt, wird ein Fehlerstatus zurückgegeben
        return f"Fehler: {response.status_code} - {response.text}"
