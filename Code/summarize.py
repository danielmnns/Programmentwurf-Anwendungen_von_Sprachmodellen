import requests

def summarize_text(text):
    url = "http://127.0.0.1:11434/api/chat"  # Endpoint der Ollama-Instanz
    payload = {
        'model': 'llama3.2',  # Gib hier dein Modell an (z.B. llama3, falls geladen)
        'messages': [
            {'role': 'system', 'content': 'Fasse die wichtigsten Punkte aus dem folgenden Text zusammen und liste alle To-Dos auf.'},
            {'role': 'user', 'content': text}
        ]
    }
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data['message']['content']  # Antworttext aus dem JSON extrahieren
    else:
        return f"Fehler bei der Zusammenfassung: {response.status_code} - {response.text}"


