import json
import os
from cryptography.fernet import Fernet

KEY_FILE = "secret.key"
DATA_FILE = "passwords.json.enc"

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)

def load_key():
    if not os.path.exists(KEY_FILE):
        generate_key()
    with open(KEY_FILE, "rb") as f:
        return f.read()

def save_password(label, password):
    key = load_key()
    fernet = Fernet(key)

    data = load_passwords()
    data[label] = password

    encrypted = fernet.encrypt(json.dumps(data).encode())
    with open(DATA_FILE, "wb") as f:
        f.write(encrypted)

def load_passwords():
    key = load_key()
    fernet = Fernet(key)

    if not os.path.exists(DATA_FILE):
        return {}

    with open(DATA_FILE, "rb") as f:
        encrypted = f.read()
        try:
            decrypted = fernet.decrypt(encrypted).decode()
            return json.loads(decrypted)
        except Exception as e:
            print("❌ Erreur de déchiffrement :", e)
            return {}
