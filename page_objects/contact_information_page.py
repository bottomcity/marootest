from playwright.sync_api import Page

class ContactInformationPage:
    def __init__(self, page: Page):
        self.page = page
        self.header_selector = "header"

    def is_contact_information_header_present(self) -> bool:
        header = self.page.locator(self.header_selector)
        header_text = header.text_content()
        return (
            "Contact information" in header_text and
            "Last step! Fill in your contact details" in header_text
        )