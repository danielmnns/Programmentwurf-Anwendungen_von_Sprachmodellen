import ollama

def summarize_text(text):
    # Anfrage an die Ollama API mit dem geladenen Modell
    response = ollama.chat(model='llama3', messages=[
        {'role': 'system', 'content': 'Fasse die wichtigsten Punkte aus dem folgenden Meeting-Protokoll zusammen und liste alle To-Dos auf.'},
        {'role': 'user', 'content': text}
    ])
    return response['message']['content']

if __name__ == "__main__":
    sample_text = "Hier kommt das Transkript hin."
    print(summarize_text(sample_text))
