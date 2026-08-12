import tkinter as tk
import random
import string


def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(12))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)


def toggle_password():
    if password_entry.cget("show") == "*":
        password_entry.config(show="")
        show_button.config(text="Hide Password")
    else:
        password_entry.config(show="*")
        show_button.config(text="Show Password")


def analyze_password():
    password = password_entry.get()

    has_upper = False
    has_lower = False
    has_number = False
    has_special = False

    special_characters = "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|"

    for letter in password:
        if letter.isupper():
            has_upper = True
        if letter.islower():
            has_lower = True
        if letter.isdigit():
            has_number = True
        if letter in special_characters:
            has_special = True

    score = 0

    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_number:
        score += 1
    if has_special:
        score += 1
    if len(password) >= 8:
        score += 1

    if score == 5:
        result = "Excellent Password"
    elif score == 4:
        result = "Strong Password"
    elif score == 3:
        result = "Medium Password"
    elif score == 2:
        result = "Weak Password"
    else:
        result = "Very Weak Password"

    result_label.config(text=result)
    score_label.config(text=f"Strength Score: {score}/5")

    requirements = (
        f"{'✓' if has_upper else '✗'} Uppercase\n"
        f"{'✓' if has_lower else '✗'} Lowercase\n"
        f"{'✓' if has_number else '✗'} Number\n"
        f"{'✓' if has_special else '✗'} Special Character\n"
        f"{'✓' if len(password) >= 8 else '✗'} At least 8 characters"
    )

    requirements_label.config(text=requirements)


# Create the main window
window = tk.Tk()
window.title("Password Strength Analyzer")
window.geometry("600x650")
window.configure(bg="#f2f2f2")

# Heading
title = tk.Label(
    window,
    text="🔐 PASSWORD STRENGTH ANALYZER",
    font=("Arial", 18, "bold"),
    bg="#f2f2f2"
)
title.pack(pady=30)

# Password label
label = tk.Label(
    window,
    text="Enter your password:",
    font=("Arial", 12),
    bg="#f2f2f2"
)
label.pack()

# Password input box
password_entry = tk.Entry(
    window,
    width=35,
    font=("Arial", 12),
    show="*"
)
password_entry.pack(pady=10)

# Analyze button
analyze_button = tk.Button(
    window,
    text="Analyze Password",
    font=("Arial", 12, "bold"),
    padx=15,
    pady=5,
    command=analyze_password
)
analyze_button.pack(pady=20)

# Generate password button
generate_button = tk.Button(
    window,
    text="Generate Strong Password",
    font=("Arial", 11, "bold"),
    padx=15,
    pady=5,
    command=generate_password
)
generate_button.pack(pady=5)

# Show/Hide password button
show_button = tk.Button(
    window,
    text="Show Password",
    font=("Arial", 10),
    command=toggle_password
)
show_button.pack(pady=5)

# Result labels
result_label = tk.Label(
    window,
    text="",
    font=("Arial", 16, "bold"),
    bg="#f2f2f2"
)
result_label.pack(pady=10)

score_label = tk.Label(
    window,
    text="Strength Score: 0/5",
    font=("Arial", 11, "bold"),
    bg="#f2f2f2"
)
score_label.pack(pady=5)

requirements_label = tk.Label(
    window,
    text="",
    font=("Arial", 12),
    justify="left",
    bg="#f2f2f2"
)
requirements_label.pack(pady=10)

# Run the application
window.mainloop()
