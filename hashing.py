import bcrypt
import csv
from datetime import datetime
import os

CSV_FILE = "password_log.csv"

def hash_password(password):
    """Hash the password using bcrypt with automatic salt."""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def store_password_result(data_dict):
    """
    Append password evaluation data to password_log.csv.
    Fields: hashed_password, entropy, strength_level, timestamp, flags, suggestion_shown
    """
    # Define headers
    headers = ["hashed_password", "entropy", "strength_level", "timestamp", "flags", "suggestion_shown"]

    # Extract values from evaluation result
    row = {
        "hashed_password": hash_password(data_dict["password"]),
        "entropy": data_dict["entropy"],
        "strength_level": data_dict["strength"],
        "timestamp": data_dict["timestamp"],
        "flags": ";".join(data_dict["flags"]),
        "suggestion_shown": data_dict.get("suggestion_shown", False)
    }

    # Write to CSV
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)
    print("[INFO] Logging password evaluation to CSV...")


