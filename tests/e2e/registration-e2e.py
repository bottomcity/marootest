from page_objects.page_factory import PageFactory
import random

def test_valid_registration(page):
    factory = PageFactory(page)

    registration_page = factory.registration_page
    contact_information_page = factory.contact_information_page

    # Generate a unique email
    random_number = random.randint(1000, 9999)
    email = f'a.yudin+{random_number}@maroo.us'
    password = 'Qwerty!123'

    # Navigate and register
    registration_page.navigate()
    registration_page.register(email, password)

    # Optionally wait for the page to load completely
    page.wait_for_load_state('networkidle')

    # Assert that the contact information header is present
    assert contact_information_page.is_contact_information_header_present(), "Contact information header not found"

    firstname = "Vasyan"
    lastname = "Pupkin"
    businessname = "business"
    website = "https://someurl.com/"

    contact_information_page.fillcontactinformation(firstname, lastname, businessname, website)


    verify_email_page = factory.verify_email_page

    assert verify_email_page.is_verify_email_text_present(), "'Verify Your Email' text not found"

    assert verify_email_page.is_email_displayed(email), f"Email {email} not displayed on verify email page"