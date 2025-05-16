from flask import Flask, render_template, request, jsonify
from rule_engine import evaluate_password
from feedback_generator import generate_feedback, generate_strong_password
from hashing import store_password_result

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/evaluate', methods=['POST'])
def evaluate():
    password = request.json.get('password')
    evaluation = evaluate_password(password)
    feedback = generate_feedback(evaluation)
    
    # Handle suggestion logic (similar to main.py)
    strength = feedback['strength']
    if strength in ["Very Weak", "Weak", "Moderate"]:
        feedback['suggestion'] = generate_strong_password()
    
    # Log results
    evaluation['suggestion_shown'] = bool(feedback.get('suggestion'))
    store_password_result(evaluation)
    
    return jsonify({
        'evaluation': evaluation,
        'feedback': feedback
    })

if __name__ == '__main__':
    app.run(debug=True)