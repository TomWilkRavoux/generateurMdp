# 🔐 Générateur de Mots de Passe avec IA (Passphrase + Sécurité)

Ce projet est un générateur de mots de passe en deux modes :
1. **Mode Classique** : Génère des mots de passe aléatoires personnalisés.
2. **Mode IA** : Utilise un LLM local (Ollama) pour générer une passphrase simple, puis la transforme avec des règles de sécurité (majuscules, chiffres, symboles).

---

## 📌 Contexte

L’objectif est de combiner sécurité et mémorabilité :
- En générant des **passphrases** faciles à retenir (grâce à l'IA)
- Et en les **renforçant automatiquement** via un script Python

---

## ⚙️ Prérequis

- Python 3.9 ou +
- [Ollama](https://ollama.com/) installé localement
- Un modèle chargé, ex : `llama3` ou `mistral`
- pip (gestionnaire de paquets Python)

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
ollama run llama3
```

---

## 🚀 Lancer le générateur

```bash
python main.py
```

Vous aurez alors le choix :
- Mode classique : génération de mot de passe personnalisée
- Mode IA : génération d'une passphrase par IA puis transformation sécurisée

---

## 📝 Fonctionnalités

- Choix de la longueur du mot de passe
- Inclusion de majuscules, chiffres et caractères spéciaux
- Copie automatique dans le presse-papier (optionnelle)
- Génération de passphrase via un LLM local
- Transformation aléatoire et sécurisée de la passphrase

---

## 📁 Structure du projet

```
.
├── main.py
├── generator_password.py
├── llm_assistant.py
├── passphrase_transformer.py
├── utils.py
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
