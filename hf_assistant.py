import torch
import random
from transformers import GPT2Tokenizer, GPT2LMHeadModel

model_name = "antoiloui/belgpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

model.eval()

def generate_passphrase_from_context(context, max_length=100):
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
        num_return_sequences=1
    )

    decoded = tokenizer.decode(output[0], skip_special_tokens=True)
    # Extraire seulement la partie générée après le prompt
    if decoded.startswith(prompt):
        return decoded[len(prompt):].strip()
    return decoded.strip()