from generator_password import generate_password
from utils import validate_length, copy_in_paper_clip
from hf_assistant import generate_passphrase_from_context
from passphrase_transformer import transformer_passphrase
from password_strength import evaluate_password_strength
from secure_storage import save_password, load_passwords


def main():
    while True:
        print("\n=== Générateur de Mots de Passe ===")
        print("1. Générer un mot de passe")
        print("2. Consulter l'historique")
        print("3. Quitter")
        choix = input("Votre choix : ")

        if choix == "1":
            mode_ia = input("Souhaitez-vous utiliser l'IA pour une suggestion ? (o/n) ").lower() == "o"

            if mode_ia:
                contexte = input("Contexte d'utilisation ?\n> ")
                try:
                    base = generate_passphrase_from_context(contexte)
                    secure = transformer_passphrase(base)

                    print("\n🤖 Phrase générée :")
                    print("BASE :", base)
                    print("🔐 TRANSFORMÉE :", secure)

                    niveau, warning, suggestions = evaluate_password_strength(secure)
                    print(f"💡 Niveau de sécurité : {niveau}")
                    if warning:
                        print("⚠️", warning)
                    for s in suggestions:
                        print("👉", s)

                    if input("Copier la passphrase dans le presse-papier ? (o/n) ").lower() == "o":
                        copy_in_paper_clip(secure)

                    if input("Sauvegarder cette passphrase ? (o/n) ").lower() == "o":
                        label = input("Nom ou usage de ce mot de passe : ")
                        save_password(label, secure)

                except Exception as e:
                    print("❌ Erreur :", e)

            else:
                longueur = int(input("Longueur du mot de passe : "))
                if not validate_length(longueur):
                    print("La longueur doit être d'au moins 12 caractères.")
                    continue

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

                if input("Copier dans le presse-papier ? (o/n) ").lower() == "o":
                    copy_in_paper_clip(mot_de_passe)

                if input("Sauvegarder ce mot de passe ? (o/n) ").lower() == "o":
                    label = input("Nom ou usage de ce mot de passe : ")
                    save_password(label, mot_de_passe)

        elif choix == "2":
            print("\n📂 Historique des mots de passe :")
            data = load_passwords()
            if not data:
                print("Aucun mot de passe enregistré.")
            else:
                for label, pwd in data.items():
                    print(f"🔐 {label} : {pwd}")

        elif choix == "3":
            print("👋 À bientôt !")
            break

        else:
            print("❌ Choix invalide. Veuillez entrer 1, 2 ou 3.")


if __name__ == "__main__":
    main()
