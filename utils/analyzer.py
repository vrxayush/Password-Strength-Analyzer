import re
import random
import string

COMMON_PASSWORDS = [
    "123456",
    "password",
    "admin",
    "qwerty",
    "12345678"
]

def generate_suggestion(password):
    extra = random.choice(["@", "#", "$", "&"])
    numbers = str(random.randint(100, 999))
    return password.capitalize() + extra + numbers

def analyze_password(password):
    score = 0
    feedback = []

    if password.lower() in COMMON_PASSWORDS:
        return {
            "strength": "Very Weak",
            "score": 0,
            "feedback": ["This password is too common."],
            "suggestion": generate_suggestion(password)
        }

    # Length check
    if len(password) >= 8:
        score += 2
    else:
        feedback.append("Use at least 8 characters.")

    if len(password) >= 12:
        score += 2

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    # Numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add numbers.")

    # Special Characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 2
    else:
        feedback.append("Add special characters.")

    # Final Strength
    if score <= 3:
        strength = "Weak"
    elif score <= 6:
        strength = "Medium"
    else:
        strength = "Strong"

    return {
        "strength": strength,
        "score": score,
        "feedback": feedback,
        "suggestion": generate_suggestion(password)
    }
