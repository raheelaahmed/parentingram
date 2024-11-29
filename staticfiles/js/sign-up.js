document.addEventListener('DOMContentLoaded', function () {
    const usernameInput = document.getElementById('id_username'); // Get the username input element
    const errorMessageElement = document.getElementById('username_error'); // Reference to error message display

    document.getElementById('signup_form').addEventListener('submit', function(event) {
        const errorMessage = validateUsername(); // Call the validation function

        if (errorMessage) {
            event.preventDefault(); // Prevent form submission on validation error
            errorMessageElement.innerText = errorMessage; // Display the error message
        } else {
            errorMessageElement.innerText = ''; // Clear previous errors
        }
    });

    function validateUsername() {
        const username = usernameInput.value; // Get the username value
        const minLength = 3;
        const maxLength = 15;
        const usernamePattern = /^[a-zA-Z][a-zA-Z0-9_]*$/; // Validation pattern

        if (username.length < minLength || username.length > maxLength) {
            return `Username must be between ${minLength} and ${maxLength} characters.`;
        }
        if (!usernamePattern.test(username)) {
            return 'Username must start with a letter and can only contain letters, numbers, and underscores.';
        }
        return ''; // Return empty string if valid
    }
});