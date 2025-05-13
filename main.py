from rule_engine import evaluate_password
from feedback_generator import generate_feedback, generate_strong_password
from hashing import store_password_result

def main():
    password = input("Enter a password to evaluate: ")

    # Step 1: Evaluate the password
    evaluation = evaluate_password(password)

    # Step 2: Display password evaluation
    print("\n--- Password Evaluation ---")
    for key, value in evaluation.items():
        print(f"{key.capitalize()}: {value}")

    # Step 3: Generate feedback
    feedback = generate_feedback(evaluation)

    # Step 4: Display feedback block (without suggestion yet)
    print("\n--- Feedback ---")
    print(f"Strength: {feedback['strength']}")
    print(f"Strength_level: {feedback['strength_level']}")
    print(f"Color: {feedback['color']}")

    if feedback["feedback"]:
        print("Tips:")
        for msg in feedback["feedback"]:
            print(f"- {msg}")

    # Step 5: Handle suggestion logic and logging
    strength = feedback["strength"]
    suggestion_shown = False

    if strength in ["Very Weak", "Weak", "Moderate"]:
        suggestion = generate_strong_password()
        print(f"Suggestion: {suggestion}")
        suggestion_shown = True

    elif strength in ["Strong", "Very Strong"]:
        print(f"Your password is {strength.lower()}.")
        choice = input("Would you like a strong password suggestion anyway? (yes/no): ").strip().lower()
        if choice == "yes":
            suggestion = generate_strong_password()
            print(f"Suggestion: {suggestion}")
            suggestion_shown = True

    # Add flag to evaluation result for logging
    evaluation["suggestion_shown"] = suggestion_shown

    # Store results securely in CSV
    store_password_result(evaluation)

if __name__ == "__main__":
    main()