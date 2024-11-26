import openai

openai.api_key = 'DEIN_OPENAI_API_KEY'

def summarize_text(text):
    prompt = f"Fasse die wichtigsten Punkte aus dem folgenden Meeting-Protokoll zusammen:\n\n{text}"
    response = openai.Completion.create(
        model="gpt-4",  # Oder gpt-3.5-turbo, falls GPT-4 nicht verfügbar ist
        prompt=prompt,
        max_tokens=300
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    sample_text = "Hier kommt das Transkript hin."
    print(summarize_text(sample_text))
