import streamlit as st
import re
import math
from zxcvbn import zxcvbn

st.set_page_config(
    page_title="Advanced Password Strength Checker",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 Advanced Password Strength Checker")
st.write("Check password strength, entropy, patterns and security.")

password = st.text_input(
    "Enter your password",
    type="password",
    placeholder="Type your password here..."
)


def entropy(password):
    pool = 0

    if re.search(r"[a-z]", password):
        pool += 26

    if re.search(r"[A-Z]", password):
        pool += 26

    if re.search(r"[0-9]", password):
        pool += 10

    if re.search(r"[^a-zA-Z0-9]", password):
        pool += 32

    if pool == 0:
        return 0

    return len(password) * math.log2(pool)


def check_password(password):

    score = 0
    problems = []

    # Length
    if len(password) >= 16:
        score += 30
    elif len(password) >= 12:
        score += 25
    elif len(password) >= 8:
        score += 15
    else:
        problems.append("Use at least 12 characters.")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 10
    else:
        problems.append("Add lowercase letters.")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 10
    else:
        problems.append("Add uppercase letters.")

    # Numbers
    if re.search(r"[0-9]", password):
        score += 10
    else:
        problems.append("Add numbers.")

    # Special characters
    if re.search(r"[^a-zA-Z0-9]", password):
        score += 15
    else:
        problems.append("Add special characters.")

    # Repeated characters
    if re.search(r"(.)\1\1", password):
        score -= 15
        problems.append("Avoid repeated characters.")

    # Sequential patterns
    sequences = [
        "123456",
        "abcdef",
        "qwerty",
        "password",
        "987654"
    ]

    for sequence in sequences:
        if sequence in password.lower():
            score -= 20
            problems.append("Avoid common or sequential patterns.")
            break

    # Common passwords
    common = [
        "password",
        "123456",
        "12345678",
        "qwerty",
        "admin",
        "welcome",
        "letmein"
    ]

    if password.lower() in common:
        score = 0
        problems.append("This is a commonly used password.")

    score = max(0, min(score, 100))

    if score < 30:
        strength = "Very Weak"
    elif score < 50:
        strength = "Weak"
    elif score < 70:
        strength = "Moderate"
    elif score < 85:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return score, strength, problems


if password:

    score, strength, problems = check_password(password)

    # Zxcvbn analysis
    result = zxcvbn(password)

    st.subheader(f"Strength: {strength}")

    st.progress(score / 100)

    st.write(f"### Score: {score}/100")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Length", len(password))

    with col2:
        st.metric("Entropy", f"{entropy(password):.1f} bits")

    with col3:
        st.metric("Zxcvbn", f"{result['score']}/4")

    st.divider()

    st.subheader("🔎 Character Analysis")

    checks = {
        "Lowercase letters": bool(re.search(r"[a-z]", password)),
        "Uppercase letters": bool(re.search(r"[A-Z]", password)),
        "Numbers": bool(re.search(r"[0-9]", password)),
        "Special characters": bool(
            re.search(r"[^a-zA-Z0-9]", password)
        ),
        "12+ characters": len(password) >= 12,
        "16+ characters": len(password) >= 16
    }

    for name, status in checks.items():

        if status:
            st.success("✓ " + name)

        else:
            st.warning("✗ " + name)

    st.divider()

    st.subheader("🛡️ Security Feedback")

    if result["feedback"]["warning"]:
        st.warning(result["feedback"]["warning"])

    for suggestion in result["feedback"]["suggestions"]:
        st.info(suggestion)

    if problems:

        st.subheader("⚠️ Improvements")

        for problem in problems:
            st.write("• " + problem)

    else:

        st.success("🎉 No major weaknesses detected!")

    st.divider()

    st.subheader("🎯 Guess Resistance")

    guesses = result["guesses"]

    if guesses < 1000:
        st.error("Very easy to guess")

    elif guesses < 1000000:
        st.warning("Easy to guess")

    elif guesses < 1000000000:
        st.info("Moderately resistant")

    else:
        st.success("Highly resistant to guessing")

st.divider()

st.caption(
    "🔒 Passwords are analyzed in memory and are not intentionally stored by this application."
)