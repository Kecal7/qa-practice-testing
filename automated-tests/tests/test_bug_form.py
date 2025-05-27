def test_bug_form_submission(page):
    page.goto("https://qa-practice.netlify.app/bugs-form")
    page.fill("#firstName", "John")
    page.fill("#lastName", "Doe")
    page.fill("#phone", "1234567890")
    page.select_option("#country", "USA")
    page.click("button[type='submit']")
    assert page.locator("text=Form submitted successfully").is_visible()
