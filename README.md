Simple Flet Form

This is a simple sign-up form built using the Flet framework in Python. The form consists of input fields for the user's first name, email, and password, along with a submit button.

Features

Text Fields: Users can enter their first name, email, and password.

Password Field: The password input is masked, but users can toggle visibility.

Button Styling: The submit button is styled with custom colors and font weights.

Container Design: The form is enclosed within a container with rounded corners and padding.

Event Handling: A function prints a message when the form is submitted.

Installation

Ensure you have Python installed. Then, install Flet using:

pip install flet

Code Explanation

UI Components

Container: Holds all form elements and defines the layout.

Text: Displays the title "Sign Up".

TextField: Input fields for user details.

Button: Triggers the form submission.

Event Handling

The form_submit_function prints "form submitted!" when the submit button is clicked.

Window Configuration

The app window is set to 600x500 pixels.

Background color is #e6e6eb.

The form is centered both horizontally and vertically.

Customization

Modify colors, sizes, and text styles in the Container and ButtonStyle attributes.

Extend functionality by adding validation or integrating with a database.

License

This project is open-source and can be modified as needed.
