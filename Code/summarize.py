import ollama

def summarize_text(text):
    response = ollama.chat(model='llama3', messages=[
        {'role': 'system', 'content': 'Fasse die wichtigsten Punkte aus dem folgenden Meeting-Protokoll zusammen und liste alle To-Dos auf.'},
        {'role': 'user', 'content': text}
    ])
    return response['message']['content']
