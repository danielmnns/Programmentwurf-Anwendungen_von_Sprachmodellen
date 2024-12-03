import requests  # Importiert das requests-Modul, um HTTP-Anfragen zu senden.

def summarize_text(text):
    # Funktion, die einen Text an eine lokale Ollama-Instanz sendet, um eine Zusammenfassung und eine Liste von To-Dos zu erstellen.
    # Parameter:
    # - text: Der Eingabetext, der zusammengefasst werden soll (z. B. ein Meeting-Protokoll).

    url = "http://127.0.0.1:11434/chat"
    # Die URL der lokalen Ollama-Instanz, die die Anfragen verarbeitet.
    # Hier läuft der Dienst lokal auf Port 11434.

    payload = {
        'model': 'llama3',
        # Gibt das zu verwendende Modell an. In diesem Fall wird "llama3" verwendet.
        'messages': [
            {'role': 'system', 'content': 'Fasse die wichtigsten Punkte aus dem folgenden Meeting-Protokoll zusammen und liste alle To-Dos auf.'},
            # Systemnachricht: Stellt dem Modell die Aufgabe, wichtige Punkte zusammenzufassen und To-Dos zu identifizieren.
            {'role': 'user', 'content': text}
            # Benutzernachricht: Überträgt den tatsächlichen Text, der verarbeitet werden soll.
        ]
    }
    # Der Payload enthält die Modelldaten und die Konversation in Form einer Liste von Nachrichten.
    # Dies ist eine gängige Struktur bei Chat-basierten Modellen.

    headers = {
        'Content-Type': 'application/json'
    }
    # Header legt fest, dass die Daten im JSON-Format gesendet werden.

    response = requests.post(url, json=payload, headers=headers)
    # Eine POST-Anfrage wird an die Ollama-Instanz gesendet. Der Payload und die Header werden mitgegeben.
    # Die Antwort wird in `response` gespeichert.

    if response.status_code == 200:
        # Überprüfung, ob die Anfrage erfolgreich war (HTTP-Statuscode 200).
        return response.json()['message']['content']
        # Wenn die Anfrage erfolgreich war, wird der Antwortinhalt extrahiert und zurückgegeben.
        # Die Antwort wird angenommen, ein JSON-Objekt zu sein, und der Schlüssel 'content' enthält die eigentliche Zusammenfassung.
    else:
        # Fehlerfall: Die Anfrage war nicht erfolgreich.
        return f"Fehler bei der Zusammenfassung: {response.status_code} - {response.text}"
        # Gibt eine Fehlermeldung zurück, die den Statuscode und den Antworttext enthält.

# Beispiel-Nutzung:
# result = summarize_text("Hier steht das Meeting-Protokoll.")
# print(result)
