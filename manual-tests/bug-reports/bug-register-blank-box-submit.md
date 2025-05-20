# 🐞 Bug Report – Registration form submits without checked box of terms and conditions

**ID:** BUG-002  
**Title:** Registration form allows submission without a required checked box of terms and conditions
**Severity:** High  
**Priority:** High  
**Reported on:** 2025-20-05  
**Environment:**  
- Browser: Firefox 125.0.1  
- OS: macOS 13 Ventura  
- App Version: Production

---

## ✅ Steps to Reproduce:
1. Open the registration page.
2. Fill out email and password but do not check the box of terms and conditions.
3. Click the "Register" button.

---

## 🧪 Expected Result:
Form should not submit. An error message should be displayed if the user does not agree to the terms and conditions.

---

## ❌ Actual Result:
The account is beeing successfully created.


---

## 📎 Attachments:
![screenshot](../assets/bug-register-blank-box-submit.png)

---

## 💡 Notes:
- Missing `required` attribute on terms and conditions box.
- Bug persists after page reload