def test_login_valid_credentials(page):
    page.goto("https://qa-practice.netlify.app/login")
    page.fill('#email', 'admin@admin.com')
    page.fill('#password', 'admin123')
    page.click('button[type="submit"]')
    success_message = page.locator("text=successfully logged in")
    assert success_message.is_visible()


def test_login_invalid_credentials(page):
    page.goto("https://qa-practice.netlify.app/login")
    page.fill('#email', 'wrong@wrong.com')
    page.fill('#password', 'badpass')
    page.click('button[type="submit"]')
    error_message = page.locator("text=Bad credentials! Please try again! Make sure that you've registered.")
    assert error_message.is_visible()

def test_login_empty_fields(page):
    page.goto("https://qa-practice.netlify.app/login")
    page.click('button[type="submit"]')
    assert page.url == "https://qa-practice.netlify.app/login"
    assert page.locator("text=Bad credentials").is_visible() or page.locator("text=Please enter your email").is_visible()