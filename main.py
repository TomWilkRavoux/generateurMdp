from generator_password import generate_password
from utils import validate_length, copy_in_paper_clip
# from llm_assistant import ask_advice_context
from hf_assistant import generate_passphrase_from_context
from passphrase_transformer import transformer_passphrase
from password_strength import evaluate_password_strength

def main():
    print("Bienvenue dans le générateur de mots de passe !")
    mode_ia = input("Souhaitez-vous utiliser l'IA pour une suggestion ? (o/n) ").lower() == "o"

    if mode_ia:
        contexte = input("Contexte d'utilisation ?\n> ")
        try:
            # base = ask_advice_context(contexte)
            base = generate_passphrase_from_context(contexte)
            secure = transformer_passphrase(base)
            print("\n🤖 Phrase générée :")
            print("BASE :", base)
            print("🔐 TRANSFORMÉE :", secure)

            niveau, warning, suggestions = evaluate_password_strength(secure)
            print(f"💡 Niveau de sécurité : {niveau}")
            if warning:
                print("⚠️ Avertissement :", warning)
            for s in suggestions:
                print("👉", s)

            if input("Copier la passphrase transformée dans le presse-papier ? (o/n) ").lower() == "o":
                copy_in_paper_clip(secure)

        except Exception as e:
            print("❌ Erreur :", e)

    else:
        longueur = int(input("Longueur du mot de passe : "))
        if not validate_length(longueur):
            print("La longueur du mot de passe doit être d'au moins 12 caractères.")
            return
        upper = input("Inclure des majuscules ? (o/n) ").lower() == "o"
        digits = input("Inclure des chiffres ? (o/n) ").lower() == "o"
        special = input("Inclure des caractères spéciaux ? (o/n) ").lower() == "o"

        mot_de_passe = generate_password(longueur, upper, digits, special)
        print(f"Mot de passe généré : {mot_de_passe}")

        niveau, warning, suggestions = evaluate_password_strength(mot_de_passe)
        print(f"💡 Niveau de sécurité : {niveau}")
        if warning:
            print("⚠️", warning)
        for s in suggestions:
            print("👉", s)

        if input("Copier le mot de passe dans le presse-papier ? (o/n) ").lower() == "o":
            copy_in_paper_clip(mot_de_passe)

if __name__ == "__main__": 
    main()
