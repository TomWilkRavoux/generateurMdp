from zxcvbn import zxcvbn
import string

def evaluate_password_strength(password):
    result = zxcvbn(password)
    score = result["score"]
    feedback = result.get("feedback", {})

    # custom rules
    has_upper = any(c in string.ascii_uppercase for c in password)
    has_digit = any(c in string.digits for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    diversity_score = sum([has_upper, has_digit, has_symbol])
    suggestions = feedback.get("suggestions", [])
    warning = feedback.get("warning", "")

    if diversity_score < 2 or len(password) < 12:
        score = min(score, 1)                           # Très faible ou faible
    elif diversity_score == 2 and len(password) < 20:
        score = min(score, 2)                           # Moyen
    elif diversity_score == 3:
        pass                                            # Pas de pénalité
    else:
        score = min(score, 3)                           # Bon, mais pas excellent

    if not has_upper:
        suggestions.append("Ajoutez au moins une majuscule.")
    if not has_digit:
        suggestions.append("Ajoutez au moins un chiffre.")
    if not has_symbol:
        suggestions.append("Ajoutez au moins un caractère spécial (!, @, #, etc.).")

    niveau = {
        0: "❌ Très faible",
        1: "⚠️ Faible",
        2: "🟡 Moyen",
        3: "✅ Bon",
        4: "🔒 Excellent"
    }

    return niveau[score], warning, suggestions
