import json
import pyAesCrypt
import os

BUFFER_SIZE = 64 * 1024  # Taille du buffer recommandée par pyAesCrypt
DATA_FILE = "passwords.json.aes"
TEMP_FILE = "passwords_temp.json"


def save_password(label, password, master_password):
    data = load_passwords(master_password)
    data[label] = password

    # Sauvegarder en JSON temporaire
    with open(TEMP_FILE, "w") as f:
        json.dump(data, f, indent=2)
    pyAesCrypt.encryptFile(TEMP_FILE, DATA_FILE, master_password, BUFFER_SIZE)
    os.remove(TEMP_FILE)


def load_passwords(master_password):
    if not os.path.exists(DATA_FILE):
        return {}

    try:
        pyAesCrypt.decryptFile(DATA_FILE, TEMP_FILE, master_password, BUFFER_SIZE)

        with open(TEMP_FILE, "r") as f:
            data = json.load(f)

        os.remove(TEMP_FILE)
        return data
    except Exception as e:
        print("❌ Erreur de déchiffrement :", e)
        return {}
