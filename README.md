# Password-strength-checker
# 🔐 Advanced Password Strength Checker

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green)

An **Advanced Password Strength Checker** built using **Python and Streamlit**.
It analyzes password strength using multiple security factors and provides useful feedback to improve password security.

---

## ✨ Features

* 🔢 **Password Strength Score** — 0–100
* 🟢 **Strength Levels**

  * Very Weak
  * Weak
  * Moderate
  * Strong
  * Very Strong
* 📏 Password length analysis
* 🔤 Lowercase character detection
* 🔠 Uppercase character detection
* 🔢 Number detection
* 🔣 Special character detection
* 🔁 Repeated character detection
* ⛓️ Sequential pattern detection
* 🚫 Common password detection
* 🧮 Entropy calculation
* 🧠 `zxcvbn` password guessability analysis
* 🛡️ Security recommendations
* 🎯 Guess-resistance estimation
* 🌐 Interactive Streamlit interface

---

## 🛠️ Technologies Used

| Technology   | Purpose                        |
| ------------ | ------------------------------ |
| 🐍 Python    | Application logic              |
| 🎈 Streamlit | Web interface                  |
| 🧠 zxcvbn    | Password guessability analysis |
| 🔎 Regex     | Pattern detection              |
| 📐 Math      | Entropy calculation            |

---

## 📂 Project Structure

```text
password-checker/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/password-checker.git
```

### 2. Enter the Project Directory

```bash
cd password-checker
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install them manually:

```bash
pip install streamlit zxcvbn
```

---

## ▶️ Run the Application

Run the following command in **CMD / Terminal**:

```bash
streamlit run app.py
```

The application will normally open at:

```text
http://localhost:8501
```

---

## 🔎 How It Works

The checker evaluates several characteristics of the password.

### 📏 Password Length

Longer passwords generally provide a larger search space and can be more resistant to guessing.

### 🔤 Character Variety

The application checks whether the password contains:

* Lowercase letters
* Uppercase letters
* Numbers
* Special characters

### 🔁 Pattern Detection

The application detects common patterns such as:

```text
123456
abcdef
qwerty
password
```

It also checks for repeated characters such as:

```text
aaa
111
```

### 🧮 Entropy

The application calculates an approximate theoretical entropy based on password length and character types.

### 🧠 zxcvbn

The project uses `zxcvbn` to provide an additional estimate of password guessability and security feedback.

---

## 📊 Strength Levels

|  Score | Strength       |
| -----: | -------------- |
|   0–29 | 🔴 Very Weak   |
|  30–49 | 🟠 Weak        |
|  50–69 | 🟡 Moderate    |
|  70–84 | 🟢 Strong      |
| 85–100 | 🟢 Very Strong |

---

## 🖥️ Example

A password such as:

```text
password123
```

will receive warnings because it contains a common password and predictable patterns.

A unique, sufficiently long password or passphrase with good unpredictability will generally receive a stronger rating.

---

## 🔒 Security & Privacy

This project is designed as a **local password-analysis tool**.

> ⚠️ Never enter a password that you currently use for an important account while testing a demo application.

The application does not intentionally save passwords.

For a real authentication system, passwords should be stored using a modern password-hashing algorithm such as **Argon2id**, rather than plain text or a general-purpose hash.

---

## 📦 Requirements

Create a `requirements.txt` file containing:

```text
streamlit
zxcvbn
```

---

## 🚀 Future Improvements

* 🔐 Secure password generator
* 📚 Larger common/breached-password database
* 📊 Interactive security dashboard
* 🌙 Dark/light theme
* 📈 Detailed analysis charts
* 🧠 Improved passphrase analysis
* 📱 Responsive UI
* ⚡ Real-time password analysis

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature/improvement
```

3. Make your changes
4. Commit your changes

```bash
git commit -m "Add new improvement"
```

5. Push the branch

```bash
git push origin feature/improvement
```

6. Open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

**Your Name**

GitHub: `https://github.com/YOUR-USERNAME`

---

## ⭐ Support

If you found this project useful, consider giving the repository a ⭐.

---

### ⚠️ Disclaimer

This project is intended for **educational and security-awareness purposes**.

Password-strength estimates are approximate and cannot guarantee that a password is completely secure.
