import random

# Feedback message mappings for each rule violation
FEEDBACK_MESSAGES = {
    "too_short": "Your password is too short. Use at least 8 characters.",
    "no_lowercase": "Add lowercase letters (a–z) to improve strength.",
    "no_uppercase": "Add uppercase letters (A–Z) to improve strength.",
    "no_digit": "Include numbers (0–9) to increase complexity.",
    "no_special": "Use special characters (e.g., @, #, $, %, etc.).",
    "common_pattern": "Avoid using common patterns like 'password', '1234', or 'admin'."
}

# Strength color codes and numeric levels
STRENGTH_COLORS = {
    "Very Weak": {"level": 1, "color": "red"},
    "Weak": {"level": 2, "color": "orange"},
    "Moderate": {"level": 3, "color": "yellow"},
    "Strong": {"level": 4, "color": "lightgreen"},
    "Very Strong": {"level": 5, "color": "green"}
}

# Word list and symbols for passphrase-style suggestions
WORDS = [
    "Thrive", "Ocean", "Maple", "Canyon", "Blink", "Falcon", "Shadow", "Yolk", "Hatch", "Drift",
    "River", "Echo", "Quartz", "Nova", "Summit", "Zephyr", "Crimson", "Meadow", "Flare", "Glimmer",
    "Tundra", "Breeze", "Starlight", "Granite", "Nimbus", "Comet", "Raven", "Frost", "Inferno", "Petal",
    "Wisp", "Mirage", "Vortex", "Harbor", "Blossom", "Pebble", "Gale", "Cinder", "Ivy", "Aurora",
    "Cascade", "Horizon", "Pine", "Quartz", "Serene", "Whisper", "Lyric", "Ember", "Valley", "Boulder"
]
SYMBOLS = "!@#$%^&*"

def generate_strong_password():
    words = random.sample(WORDS, 3)  # pick 3 distinct words
    random.shuffle(words)  # randomize order
    digits = str(random.randint(10, 99))
    symbol = random.choice(SYMBOLS)
    return f"{words[0]}{symbol}{digits}_{words[1]}_{words[2]}"

def generate_feedback(evaluation_result):
    flags = evaluation_result.get("flags", [])
    feedback = [FEEDBACK_MESSAGES[f] for f in flags if f in FEEDBACK_MESSAGES]

    strength = evaluation_result["strength"]
    meta = STRENGTH_COLORS.get(strength, {"level": 0, "color": "gray"})

    result = {
        "strength": strength,
        "strength_level": meta["level"],
        "color": meta["color"],
        "feedback": feedback,
        "suggestion": None  # Leave this empty, main.py decides whether to add it
    }

    return result
