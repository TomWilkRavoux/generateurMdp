import random
import string

def transformer_passphrase(phrase):
    special_chars = "!@#$%&*-_=+.,?"
    transformed = []

    for word in phrase.split():
        new_word = ""
        for c in word:
            r = random.random()
            if r < 0.2:
                new_word += c.upper()
            elif r < 0.3:
                new_word += random.choice(string.digits)
            elif r < 0.4:
                new_word += random.choice(special_chars)
            else:
                new_word += c
        transformed.append(new_word)

    return ''.join(transformed)
