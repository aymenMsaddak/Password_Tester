document.getElementById('evaluate-btn').addEventListener('click', evaluatePassword);

async function evaluatePassword() {
    const password = document.getElementById('password').value.trim();
    const btn = document.getElementById('evaluate-btn');
    
    if (!password) {
        alert('Please enter a password');
        return;
    }

    try {
        btn.disabled = true;
        btn.textContent = 'Evaluating...';
        
        const response = await fetch('/evaluate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ password })
        });
        
        if (!response.ok) throw new Error('Server error');
        const data = await response.json();
        updateUI(data);
        
    } catch (error) {
        console.error('Error:', error);
        alert('Evaluation failed. Please try again.');
    } finally {
        btn.disabled = false;
        btn.textContent = 'Evaluate';
    }
}

function updateUI(data) {
    const { feedback } = data;
    const strengthBar = document.getElementById('strength-bar');
    
    // Update strength indicator
    document.getElementById('strength-label').textContent = feedback.strength;
    strengthBar.style.width = `${feedback.strength_level * 20}%`;
    strengthBar.className = `progress-bar bg-${feedback.color}`;
    
    // Update tips
    const tipsList = document.getElementById('tips-list');
    tipsList.innerHTML = feedback.feedback.length > 0
        ? feedback.feedback.map(tip => `<li class="list-group-item">${tip}</li>`).join('')
        : '<li class="list-group-item">No suggestions. Great password!</li>';
    
    // Update suggestion
    const suggestionDiv = document.getElementById('suggestion');
    if (feedback.suggestion) {
        suggestionDiv.innerHTML = `
            <strong>Suggestion:</strong> ${feedback.suggestion}
            <button class="btn btn-sm btn-outline-secondary ms-2">Copy</button>
        `;
        suggestionDiv.style.display = 'block';
        suggestionDiv.querySelector('button').addEventListener('click', () => {
            navigator.clipboard.writeText(feedback.suggestion);
            alert('Copied to clipboard!');
        });
    } else {
        suggestionDiv.style.display = 'none';
    }
}