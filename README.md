# 🔐 Générateur de Mots de Passe avec IA (Passphrase + Sécurité)

Ce projet est un générateur de mots de passe en deux modes :
1. **Mode Classique** : Génère des mots de passe aléatoires personnalisés.
2. **Mode IA** : Génère une **passphrase en français** via un LLM local (Ollama ou Hugging Face), puis la renforce automatiquement avec des règles de sécurité.

---

## 📚 Sommaire

- [Contexte](#-contexte)
- [Prérequis](#-prérequis)
- [Installation](#-installation)
- [Lancement](#-lancer-le-générateur)
- [Fonctionnalités](#-fonctionnalités)
- [Historique chiffré](#-historique-sécurisé-local)
- [Structure du projet](#-structure-du-projet)
- [Exemple](#-exemple-dutilisation-ia)
- [Licence](#️-licence)

---
## 📌 Contexte

Ce projet vise à **faciliter la création de mots de passe à la fois forts et mémorisables**, grâce à :
- l’usage de **passphrases en français** via un modèle de langage (LLM)
- un renforcement automatique (majuscule, chiffres, symboles)
- une **sauvegarde chiffrée et consultable** des mots de passe

---

## ⚙️ Prérequis

- Python 3.9 ou +
- `pip` (gestionnaire de paquets Python)
- Un LLM local, au choix :
  - ✅ **Ollama** : `ollama run llama3`
  - ✅ **Hugging Face** : modèle `antoiloui/belgpt2` (automatiquement chargé via `transformers`)

---

## 📦 Installation

```bash
# Clonez le projet
git clone https://github.com/TomWilkRavoux/generateurMdp.git
cd generateurMdp

# Créez un environnement virtuel (optionnel mais recommandé)
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate   # Windows

# Installez les dépendances
pip install -r requirements.txt
```

### 🧠 Démarrer Ollama avec un modèle :

```bash
ollama run llama3.2:1b
```

---

## 🚀 Lancer le générateur

```bash
python main.py
```

Menu proposé :
=== Générateur de Mots de Passe ===
1. Générer un mot de passe
2. Consulter l'historique
3. Quitter
---

## 📝 Fonctionnalités

- ✅ Génération personnalisée (longueur, majuscule, chiffres, symboles)
- ✅ Génération par IA avec transformation sécurisée
- ✅ Copie automatique dans le presse-papier (optionnelle)
- ✅ Vérification de la robustesse du mot de passe (zxcvbn)
- ✅ Historique chiffré localement avec clé maîtresse
- ✅ Lecture de l’historique (via AES 128 bits avec cryptography.fernet)
- ✅ Support d’un LLM via Ollama ou Hugging Face

---

## 🔐 Historique sécurisé (local)
Chaque mot de passe généré peut être sauvegardé dans un fichier chiffré :
- 🔐 Le fichier passwords.json.enc contient les mots de passe sauvegardés.
- 🗝️ La clé secrète est stockée dans secret.key.
- 👁️ L'utilisateur peut consulter son historique via le menu.
---

## ✅ Exemple d’utilisation (mode IA)
```bash
Bienvenue dans le générateur de mots de passe !
Souhaitez-vous utiliser l'IA pour une suggestion ? (o/n) o
Contexte d'utilisation ?
> Pour mon coffre-fort numérique

🤖 Phrase générée :
BASE : le jardin est calme sous la lune d hiver douce et noire
🔐 TRANSFORMÉE : LeJardin3Est@CalmeSous!LaLune#Dhiver2DouceEtNoire
📋 Copié dans le presse-papier.

```
---
## 📁 Structure du projet

```
.
├── main.py
├── generator_password.py
├── passphrase_transformer.py
├── hf_assistant.py            ← version Hugging Face
├── llm_assistant.py           ← version Ollama
├── password_strength.py
├── secure_storage.py
├── utils.py
├── secret.key                 ← clé de chiffrement locale
├── passwords.json.enc         ← historique chiffré (non tracké)
├── requirements.txt
└── README.md
```

---

## ✅ Exemple d’utilisation (IA)

```
Bienvenue dans le générateur de mots de passe !
Souhaitez-vous utiliser l'IA pour une suggestion ? (o/n) o
Contexte d'utilisation ?
> pour mon coffre-fort numérique

🤖 Phrase générée :
BASE : le jardin est calme sous la lune d hiver douce et noire
🔐 TRANSFORMÉE : LeJardin3Est@CalmeSous!LaLune#Dhiver2DouceEtNoire
📋 Copié dans le presse-papier.
```

---

## 🛡️ Licence

MIT - Utilisation libre à des fins personnelles.
