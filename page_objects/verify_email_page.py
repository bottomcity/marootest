from playwright.sync_api import Page


class VerifyEmailPage:
    def __init__(self, page: Page):
        self.page = page
        self.verify_text_selector = "div.form-title"  # Adjust if necessary
        self.email_p_selector = "p:has-text('Check your inbox')"
        self.button = 'button[type="button"]'
        self.toast_p_selector = "p:has-text('The verification email was resend')"

    def is_verify_email_text_present(self) -> bool:
        header = self.page.locator(self.verify_text_selector)
        header_text = header.text_content().strip()
        return "Verify Your Email" in header_text

    def is_email_displayed(self, email: str) -> bool:
        # Locate the <p> element with the text "Check your inbox"
        email_p_element = self.page.locator(self.email_p_selector)

        # Ensure the <p> element exists
        if not email_p_element.is_visible():
            return False

        # Locate the <span> inside the <p> element
        span_element = email_p_element.locator("span")

        # Ensure the <span> element exists
        if not span_element.is_visible():
            return False

        # Get the email text
        email_text = span_element.text_content().strip()

        # Compare with the expected email
        return email_text == email

    def resendemail (self):

        self.page.expect_navigation()
        self.page.click(self.button)
        toast_p_element = self.page.locator(self.email_p_selector)

        # Ensure the <p> element exists
        if not toast_p_element.is_visible():
            return False


