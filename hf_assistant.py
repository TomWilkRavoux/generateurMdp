# import torch
# import random

model = None
tokenizer = None
model_name = "antoiloui/belgpt2"

def load_model():
    global model, tokenizer
    if model is None or tokenizer is None:
        print("⏳ Chargement du modèle IA...")
        from transformers import GPT2Tokenizer, GPT2LMHeadModel  # déplacé ici
        model_name = "antoiloui/belgpt2"
        tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        model = GPT2LMHeadModel.from_pretrained(model_name)
        model.eval()
        print("✅ Modèle chargé.")

def generate_passphrase_from_context(context, max_length=100):
    load_model()

    prompt = (
        f"Génère une passphrase française simple et fluide pour : {context}. "
        "Elle doit contenir entre 8 et 12 mots. N'ajoute pas d'explication."
    )
    inputs = tokenizer.encode(prompt, return_tensors="pt")

    output = model.generate(
        input_ids=inputs,
        do_sample=True,
        max_length=max_length,
        top_k=50,
        top_p=0.95,
        num_return_sequences=1,
        pad_token_id=tokenizer.eos_token_id
    )

    decoded = tokenizer.decode(output[0], skip_special_tokens=True)
    if decoded.startswith(prompt):
        return decoded[len(prompt):].strip()
    return decoded.strip()
