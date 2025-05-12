import re
import math
from datetime import datetime

# 1. Entropy calculation function
def calculate_entropy(password):
    pool = 0
    if any(c.islower() for c in password): pool += 26
    if any(c.isupper() for c in password): pool += 26
    if any(c.isdigit() for c in password): pool += 10
    if any(c in "!@#$%^&*()-_=+[{]};:'\",<.>/?`~" for c in password): pool += 32
    length = len(password)
    return round(math.log2(pool ** length), 2) if pool else 0

# 2. Password rule checks
def check_rules(password):
    violations = []

    if len(password) < 8:
        violations.append("too_short")

    if not re.search(r"[a-z]", password):
        violations.append("no_lowercase")

    if not re.search(r"[A-Z]", password):
        violations.append("no_uppercase")

    if not re.search(r"\d", password):
        violations.append("no_digit")

    if not re.search(r"[!@#$%^&*()\-_=+\[\]{};:'\",<.>/?`~]", password):
        violations.append("no_special")

    if re.search(r"(password|1234|qwerty|azerty|admin)", password.lower()):
        violations.append("common_pattern")

    return violations

# 3. Strength category mapping based on entropy
def get_strength_label(entropy):
    if entropy < 28:
        return "Very Weak"
    elif entropy < 36:
        return "Weak"
    elif entropy < 60:
        return "Moderate"
    elif entropy < 128:
        return "Strong"
    else:
        return "Very Strong"

# 4. Master function to evaluate password
def evaluate_password(password):
    entropy = calculate_entropy(password)
    violations = check_rules(password)
    strength = get_strength_label(entropy)

    result = {
        "password": password,
        "entropy": entropy,
        "flags": violations,
        "strength": strength,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    return result

# 5. Test the module
if __name__ == "__main__":
    sample_passwords = [
        "pass123",
        "Pa$$word2024",
        "qwerty",
        "SecureOne#2025",
        "helloWorld123!",
        "Short1!"
    ]

    for pwd in sample_passwords:
        print(f"\nPassword: {pwd}")
        evaluation = evaluate_password(pwd)
        for k, v in evaluation.items():
            print(f"{k.capitalize()}: {v}")
