function validateRegistrationForm() {
    var username = document.getElementById("id_username").value;
    var email = document.getElementById("id_email").value;
    var password = document.getElementById("id_password1").value;
    var confirmPassword = document.getElementById("id_password2").value;

    // Validate username
    if (username === "") {
        alert("Please enter a username.");
        return false;
    }

    // Validate email format
    var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(email)) {
        alert("Please enter a valid email address.");
        return false;
    }

    // Validate password complexity
    var passwordPattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
    if (!passwordPattern.test(password)) {
        alert("Password must contain at least 8 characters, including uppercase and lowercase letters, numbers, and special characters.");
        return false;
    }

    // Validate password confirmation
    if (password !== confirmPassword) {
        alert("Passwords do not match.");
        return false;
    }

    // Form is valid
    return true;
}
