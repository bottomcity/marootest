# page_objects/registration_page.py

from playwright.sync_api import Page

class RegistrationPage:
    def __init__(self, page: Page):
        self.page = page
        # Define selectors
        self.email_input = 'input[name="email"]'
        self.password_input = 'input[name="password"]'
        self.submit_button = 'button[type="submit"]'

    def navigate(self):
        self.page.goto("/")

    def register(self, email: str, password: str):
        self.page.fill(self.email_input, email)
        self.page.fill(self.password_input, password)
        with self.page.expect_navigation():
            self.page.click(self.submit_button)
