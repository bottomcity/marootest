# page_objects/page_factory.py

from playwright.sync_api import Page
from page_objects.registration_page import RegistrationPage
from page_objects.contact_information_page import ContactInformationPage
from page_objects.verify_email_page import VerifyEmailPage  # Import the new page

class PageFactory:
    def __init__(self, page: Page):
        self.page = page
        self._pages = {}

    def get_page(self, page_class):
        if page_class not in self._pages:
            self._pages[page_class] = page_class(self.page)
        return self._pages[page_class]

    @property
    def registration_page(self):
        return self.get_page(RegistrationPage)

    @property
    def contact_information_page(self):
        return self.get_page(ContactInformationPage)

    @property
    def verify_email_page(self):
        return self.get_page(VerifyEmailPage)