import requests

def summarize_text(text):
    url = "http://127.0.0.1:11434/chat"  # URL der lokalen Ollama-Instanz
    payload = {
        'model': 'llama3',
        'messages': [
            {'role': 'system', 'content': 'Fasse die wichtigsten Punkte aus dem folgenden Meeting-Protokoll zusammen und liste alle To-Dos auf.'},
            {'role': 'user', 'content': text}
        ]
    }
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        return response.json()['message']['content']
    else:
        return f"Fehler bei der Zusammenfassung: {response.status_code} - {response.text}"