'''
@Author                : Daniel<danielmannes@gmail.com>
@CreatedDate           : 2025-01-14 13:30:34
@LastEditors           : Daniel<danielmannes@gmail.com>
@LastEditDate          : 2025-01-14 13:30:34
@FilePath              : Programmentwurf-Anwendungen_von_Sprachmodellen/Code/summarize.py
'''

import requests
import json
from langdetect import detect

def summarize_text(text):
    language = detect(text)  # Erkennung der Sprache des Textes
    
    # Wir können die Benutzeranweisung anpassen, je nachdem, welche Sprache erkannt wird
    if language == 'de':
        summary_instruction = 'Fasse die wesentlichen Informationen aus dem folgenden Text prägnant zusammen und erstelle eine Liste aller To-Dos.'
    elif language == 'en':
        summary_instruction = 'Provide a concise summary of the key points in the following text and outline all the actionable to-dos.'
    else:
        summary_instruction = 'Fasse die wesentlichen Informationen aus dem folgenden Text prägnant zusammen und erstelle eine Liste aller To-Dos.'

    url = "http://127.0.0.1:11434/api/chat"  # Ollama API-Endpunkt
    payload = {
        'model': 'llama3.2',
        'messages': [
            {'role': 'system', 'content': summary_instruction},
            {'role': 'user', 'content': text}
        ],
        'stream': True  # Aktiviert Streaming der Antwort
    }
    headers = {'Content-Type': 'application/json'}
    
    response = requests.post(url, json=payload, headers=headers, stream=True)
    
    if response.status_code == 200:
        full_content = ""
        # Verarbeitung der Streaming-Daten
        for line in response.iter_lines():
            if line:
                try:
                    fragment = json.loads(line)  # Konvertiere das Fragment in JSON
                    content_piece = fragment.get('message', {}).get('content', '')
                    full_content += content_piece  # Füge den Inhalt zusammen
                except json.JSONDecodeError:
                    print("Fehler beim Dekodieren eines Fragments:", line)
        return full_content
    else:
        return f"Fehler: {response.status_code} - {response.text}"

