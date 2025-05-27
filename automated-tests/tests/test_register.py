import pytest

@pytest.mark.parametrize("email,password,confirm_password,expect_success", [
    ("newuser@example.com", "StrongPass123", "StrongPass123", True),
    ("invalidemail", "pass123", "pass123", False),
    ("user@example.com", "pass123", "different", False),
    ("", "", "", False),
])
def test_register_form(page, email, password, confirm_password, expect_success):
    page.goto("https://qa-practice.netlify.app/register")
    page.fill("#email", email)
    page.fill("#password", password)
    page.fill("#confirmPassword", confirm_password)
    page.click("button[type='submit']")

    if expect_success:
        assert page.locator("text=successfully registered").is_visible()
    else:
        assert page.locator("text=Please check your input").is_visible() or \
               page.locator("text=Passwords do not match").is_visible() or \
               page.locator("text=Invalid email").is_visible()
