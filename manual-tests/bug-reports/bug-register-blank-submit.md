# 🐞 Bug Report – Registration form submits with empty fields

**ID:** BUG-002  
**Title:** Registration form allows submission without required fields  
**Severity:** High  
**Priority:** Critical  
**Reported on:** 2025-05-20  
**Environment:**  
- Browser: Firefox 125.0.1  
- OS: macOS 13 Ventura  
- App Version: Production

---

## ✅ Steps to Reproduce:
1. Open the registration page.
2. Leave all input fields empty.
3. Click the "Register" button.

---

## 🧪 Expected Result:
Form should not submit. Error messages should be shown for all required fields (e.g., email, password).

---

## ❌ Actual Result:
The form submits and returns a 200 OK response, redirecting to a blank dashboard.

---

## 📎 Attachments:
![screenshot](../assets/bug-register-blank-submit.png)

---

## 💡 Notes:
- Missing `required` attribute on several input elements
- Bug persists after page reload