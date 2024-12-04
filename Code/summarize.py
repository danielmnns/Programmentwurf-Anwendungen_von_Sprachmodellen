import requests
import json

def summarize_text(text):
    url = "http://127.0.0.1:11434/api/chat"  # Ollama API-Endpunkt
    payload = {
        'model': 'llama3.2',
        'messages': [
            {'role': 'system', 'content': 'Fasse die wichtigsten Punkte aus dem folgenden Text zusammen und liste alle To-Dos auf.'},
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

