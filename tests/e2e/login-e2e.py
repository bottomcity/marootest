def test_valid_login(page):
    # Navigate to the login page
    page.goto("https://stg.maroo.us/v/signup")

    # Fill in the login form
    page.fill('input[name="email"]', 'test_username')
    page.fill('input[name="password"]', 'Qwerty!123')

    # Click the login button
    page.click('button[type="submit"]')

    # Wait for navigation or a specific element that indicates successful login
    page.wait_for_selector("text=Welcome")

    # Assert that the login was successful
    assert "Welcome" in page.content()