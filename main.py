from generator_password import generate_password
from utils import validate_length, copy_in_paper_clip

def main():
    print("Bienvenue dans le générateur de mots de passe !")
    longueur = int(input("Longueur du mot de passe : "))
    if not validate_length(longueur):
        print("La longueur du mot de passe doit être d'au moins 12 caractères.")
        return
    upper = input("Inclure des majuscules ? (o/n) ").lower() == "o"
    digits = input("Inclure des chiffres ? (o/n) ").lower() == "o"
    special = input("Inclure des caractères spéciaux ? (o/n) ").lower() == "o"


    mot_de_passe = generate_password(longueur, upper, digits, special)
    print(f"Mot de passe généré : {mot_de_passe}")

    if input("Copier le mot de passe dans le presse-papier ? (o/n) ").lower() == "o":
        copy_in_paper_clip(mot_de_passe)

if __name__ == "__main__": 
    main()

