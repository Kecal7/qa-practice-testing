# 🐞 Bug Report – Incorrect error message on login failure

**ID:** BUG-001  
**Title:** Unprofessional "Invalid credentials" message shown on failed login  
**Severity:** Medium  
**Priority:** Medium  
**Reported on:** 2025-20-05  
**Environment:**  
- Browser: Chrome 124.0.6367.78
- OS: Windows 11  

---

## ✅ Steps to Reproduce:
1. Open the login page.
2. Enter a valid email.
3. Enter an incorrect password.
4. Click the "Login" button.

---

## 🧪 Expected Result:
A clear error message should appear, such as:

> "Invalid email or password"

---

## ❌ Actual Result:
Unprofessional error message is shown: "Bad credentials! Please try again! Make sure that you've registered."

---

## 📎 Attachments:
![screenshot](../assets/bug-login-invalid-error.png)

---

## 💡 Notes:
- Happens on both Chrome and Firefox
