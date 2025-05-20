# 🐞 Bug Report – Incorrect error message on login failure

**ID:** BUG-001  
**Title:** "Invalid credentials" message not shown on failed login  
**Severity:** Medium  
**Priority:** High  
**Reported on:** 2025-05-20  
**Environment:**  
- Browser: Chrome 124.0.6367.78  
- OS: Windows 11  
- App Version: Production (https://qa-practice.netlify.app/)

---

## ✅ Steps to Reproduce:
1. Open the login page.
2. Enter a valid email (e.g., testuser@example.com).
3. Enter an incorrect password.
4. Click the "Login" button.

---

## 🧪 Expected Result:
A clear error message should appear, such as:

> "Invalid email or password"

---

## ❌ Actual Result:
No error message is shown. The user remains on the same page without feedback.

---

## 📎 Attachments:
![screenshot](../assets/bug-login-invalid-error.png)

---

## 💡 Notes:
- No JavaScript errors in console
- Happens on both Chrome and Firefox
