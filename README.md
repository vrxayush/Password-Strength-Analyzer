# 🔐 Password Strength Analyzer

A simple and secure Password Strength Analyzer built using Python and Flask that evaluates password security based on complexity, length, and character combinations.

---

## 🚀 Features

- 🔍 Analyze password strength instantly  
- 🔐 Checks uppercase, lowercase, numbers, and symbols  
- 📏 Evaluates password length and complexity  
- ⚠️ Detects weak/common passwords  
- 💡 Suggests stronger password alternatives  
- 🌐 Simple web-based interface using Flask  

---

## 🧠 How It Works

1. User enters a password  
2. System analyzes:
   - Length
   - Uppercase letters
   - Lowercase letters
   - Numbers
   - Special characters  
3. Password is scored based on security rules  
4. Strength level is displayed:
   - Weak
   - Medium
   - Strong  
5. Suggestions are provided for improving weak passwords  

---


## 🛠️ Tech Stack

- Python  
- Flask  
- HTML  
- CSS  
- JavaScript  

---

## 📁 Project Structure

```bash
password-strength-analyzer/
│
├── app.py
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       └── script.js
│
└── utils/
    └── analyzer.py
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/vrxayush/Password-Strength-Analyzer.git

cd password-strength-analyzer
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
```

### 3️⃣ Activate Virtual Environment

#### Windows
```bash
.\venv\Scripts\activate
```

#### Linux / Mac
```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 5️⃣ Run Project
```bash
python app.py
```

---

## 🌐 Open in Browser

```bash
http://127.0.0.1:5000
```

---

## 🔑 Example

### Weak Password
```text
password123
```

### Strong Password
```text
R@juSecure#2026
```

---

## ⚠️ Important Notes

- Do not use common passwords  
- Longer passwords are more secure  
- Use a mix of:
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Symbols  

---

## 📈 Future Improvements

- 📊 Real-time password strength meter  
- 🔐 Password hashing system  
- 🗄️ Database integration for password history  
- 🌙 Dark mode UI  
- 🔑 Random strong password generator  
- ☁️ API integration for breached password detection  

---

## 🎯 Use Case

This project demonstrates:

- Password security concepts  
- Basic cryptography understanding  
- Flask web development  
- Regex pattern matching  
- Frontend and backend integration  

---

## 👨‍💻 Author

Ayush Shah  
Computer Science Engineering Student  
Interest: Cyber Security, AI, IoT & Software Development
