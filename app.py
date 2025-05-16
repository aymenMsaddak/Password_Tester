from flask import Flask, render_template, request, jsonify
from rule_engine import evaluate_password
from feedback_generator import generate_feedback, generate_strong_password
from hashing import store_password_result

app = Flask(__name__)

# Serve the main HTML page
@app.route('/')
def home():
    return render_template('index.html')  # templates/index.html must exist

# Handle AJAX request from frontend JS
@app.route('/evaluate', methods=['POST'])
def evaluate():
    data = request.get_json()
    password = data.get('password')  # receives from JS fetch()

    if not password:
        return jsonify({"error": "No password provided"}), 400

    # Evaluate and generate feedback
    evaluation = evaluate_password(password)
    feedback = generate_feedback(evaluation)

    # Handle suggestion logic
    strength = feedback['strength']
    if strength in ["Very Weak", "Weak", "Moderate"]:
        feedback['suggestion'] = generate_strong_password()

    # Store result securely
    evaluation['suggestion_shown'] = bool(feedback.get('suggestion'))
    store_password_result(evaluation)

    return jsonify({
        'evaluation': evaluation,
        'feedback': feedback
    })

if __name__ == '__main__':
    app.run(debug=True)
