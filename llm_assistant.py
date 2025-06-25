import requests

def demander_conseil_contexte(context):
    prompt = (
        f"Je veux créer un mot de passe pour : {context}. "
        "Propose une stratégie de création de mot de passe solide, "
        "puis génère un exemple. Explique pourquoi il est fort."
    )

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama3", "prompt": prompt, "stream": False}
    )

    if response.ok:
        return response.json()["response"].strip()
    else:
        raise Exception("Erreur de réponse d'Ollama.")

