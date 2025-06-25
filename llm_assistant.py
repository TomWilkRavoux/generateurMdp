import requests

def ask_advice_context(context):
    prompt = (
        f"Génère une phrase en français pour un mot de passe mémorable, dans le contexte suivant : {context}.\n"
        "Donne-moi uniquement une passphrase simple composée de 12 à 18 mots en minuscules, sans ponctuation ni explication."
    )

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama3.2:1b", "prompt": prompt, "stream": False}
    )

    if response.ok:
        return response.json()["response"].strip()
    else:
        raise Exception(f"Erreur de réponse d'Ollama : {response.status_code} - {response.text}")