document.getElementById('password').addEventListener('input', function(e) {
  const password = e.target.value;
  const strengthDisplay = document.getElementById('password-strength');
  const suggestionPrompt = document.getElementById('suggestion-prompt');
  
  // Reset displays
  suggestionPrompt.style.display = 'none';
  
  if (password.length === 0) {
    strengthDisplay.textContent = '';
    return;
  }
  
  // Check password strength (simplified example)
  const strength = checkPasswordStrength(password);
  
  // Display strength
  strengthDisplay.textContent = `Password strength: ${strength.level}`;
  strengthDisplay.style.color = strength.color;
  
  // Show suggestion prompt only for strong/very strong passwords
  if (strength.level === 'Strong' || strength.level === 'Very Strong') {
    suggestionPrompt.style.display = 'block';
    
    // Add event listeners for Yes/No buttons
    document.getElementById('yes-btn').onclick = function() {
      showPasswordSuggestions(password);
      suggestionPrompt.style.display = 'none';
    };
    
    document.getElementById('no-btn').onclick = function() {
      suggestionPrompt.style.display = 'none';
    };
  }
});

function checkPasswordStrength(password) {
  // This is a simplified example - implement your actual strength checking logic
  let score = 0;
  
  // Length check
  if (password.length >= 12) score += 2;
  else if (password.length >= 8) score += 1;
  
  // Complexity checks
  if (/[A-Z]/.test(password)) score += 1;
  if (/[a-z]/.test(password)) score += 1;
  if (/[0-9]/.test(password)) score += 1;
  if (/[^A-Za-z0-9]/.test(password)) score += 1;
  
  // Determine strength level
  if (score >= 5) return { level: 'Very Strong', color: 'green' };
  if (score >= 4) return { level: 'Strong', color: 'blue' };
  if (score >= 3) return { level: 'Medium', color: 'orange' };
  return { level: 'Weak', color: 'red' };
}

function showPasswordSuggestions(password) {
  const feedbackDiv = document.getElementById('suggestion-feedback');
  const feedbackContent = document.getElementById('feedback-content');
  const suggestedPassword = document.getElementById('suggested-password');
  
  // Analyze password and provide feedback
  let feedback = [];
  
  if (password.length < 12) {
    feedback.push("Consider making your password longer (at least 12 characters).");
  }
  if (!/[A-Z]/.test(password)) {
    feedback.push("Add at least one uppercase letter.");
  }
  if (!/[0-9]/.test(password)) {
    feedback.push("Include numbers for better security.");
  }
  if (!/[^A-Za-z0-9]/.test(password)) {
    feedback.push("Special characters (!@#$%^&*) make passwords stronger.");
  }
  
  // Generate a suggested stronger password
  const suggested = generateStrongPassword();
  
  // Display feedback
  feedbackContent.innerHTML = feedback.length > 0 
    ? '<ul>' + feedback.map(item => `<li>${item}</li>`).join('') + '</ul>'
    : '<p>Your password is already very strong! Here\'s an alternative suggestion anyway.</p>';
  
  suggestedPassword.textContent = suggested;
  
  // Set up "use suggestion" button
  document.getElementById('use-suggestion').onclick = function() {
    document.getElementById('password').value = suggested;
    feedbackDiv.style.display = 'none';
  };
  
  // Show the feedback div
  feedbackDiv.style.display = 'block';
}

function generateStrongPassword() {
  // This is a simple generator - consider using a more robust library
  const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()';
  let result = '';
  for (let i = 0; i < 16; i++) {
    result += chars.charAt(Math.floor(Math.random() * chars.length));
  }
  return result;
}