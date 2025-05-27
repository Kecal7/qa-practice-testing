def test_nav_links_work(page):
    page.goto("https://qa-practice.netlify.app/")
    page.click("text=Login")
    assert page.url.endswith("/login")

    page.goto("https://qa-practice.netlify.app/")
    page.click("text=Register")
    assert page.url.endswith("/register")

    page.goto("https://qa-practice.netlify.app/")
    page.click("text=Buggy Form")
    assert page.url.endswith("/bugs-form")

def test_redirect_if_not_logged_in(page):
    page.goto("https://qa-practice.netlify.app/bugs-form")
    assert page.url.endswith("/login")  # assuming bugs-form page requires auth

def test_logout(page):
    page.goto("https://qa-practice.netlify.app/login")
    page.fill('#email', 'admin@admin.com')
    page.fill('#password', 'admin123')
    page.click('button[type="submit"]')
    page.click("text=Logout")
    assert page.url.endswith("/login")
