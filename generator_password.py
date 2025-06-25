import secrets
import string

def generate_password(longueur=12, use_upper=True, use_digits=True, use_special=True):
    alphabet = string.ascii_lowercase
    if use_upper:
        alphabet += string.ascii_uppercase
    if use_digits:
        alphabet += string.digits
    if use_special:
        alphabet += string.punctuation

    if not alphabet:
        raise ValueError("Aucun caractère sélectionné pour générer le mot de passe.")
    return ''.join(secrets.choice(alphabet) for _ in range(longueur))
