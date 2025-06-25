import pyperclip

def copy_in_paper_clip(texte):
    pyperclip.copy(texte)
    print("Mot de passe copié dans le presse-papier.")

def validate_length(longueur):
    return longueur >= 12
