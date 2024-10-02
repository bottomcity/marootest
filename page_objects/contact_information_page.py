from playwright.sync_api import Page

class ContactInformationPage:
    def __init__(self, page: Page):
        self.page = page
        self.header_selector = "header"
        self.first_name_input = 'input[name="firstName"]'
        self.last_name_input = 'input[name="lastName"]'
        self.business_name_input = 'input[name="businessName"]'
        self.website_input = 'input[name="website"]'
        self.business_name_input = 'input[name="businessName"]'
        self.business_category_dropdown = 'input[placeholder="Select business category"]'
        self.learn_about_maroo_dropdown = 'input[placeholder="Select an option"]'
        self.submit_button = 'button[type="submit"]'

    def is_contact_information_header_present(self) -> bool:
        header = self.page.locator(self.header_selector)
        header_text = header.text_content()
        return (
            "Contact information" in header_text and
            "Last step! Fill in your contact details" in header_text
        )

    def fillcontactinformation(self, firstname: str, lastname: str, businessname: str, website: str):
        self.page.fill(self.first_name_input, firstname)
        self.page.fill(self.last_name_input, lastname)
        self.page.fill(self.business_name_input, businessname)
        self.page.fill(self.website_input, website)
        self.page.click(self.business_category_dropdown)
        self.page.wait_for_selector('div[role="presentation"]').click()
        self.page.click(self.learn_about_maroo_dropdown)
        self.page.wait_for_selector('div[role="presentation"]').click()

        with self.page.expect_navigation():
            self.page.click(self.submit_button)