from playwright.sync_api import Page
from page_objects.registration_page import RegistrationPage

class PageFactory:
    def __init__(self, page: Page):
        self.page = page
        self._pages = {}

    def get_page(self, page_class):
        if page_class not in self._pages:
            self._pages[page_class] = page_class(self.page)
        return self._pages[page_class]

    @property
    def login_page(self):
        return self.get_page(LoginPage)

    @property
    def registration_page(self):
        return self.get_page(RegistrationPage)

    @property
    def home_page(self):
        return self.get_page(HomePage)