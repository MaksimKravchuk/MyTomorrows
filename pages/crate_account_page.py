import allure
from playwright.sync_api import Page


class CreateAccountPage:

    def __init__(self, page: Page):
        self.page = page
        self.email_input = self.page.locator(
            "myt-input", has_text="Email Address"
        ).get_by_placeholder("yourname@hospital.com")
        self.confirm_email_input = self.page.locator(
            "myt-input", has_text="Confirm Email"
        ).get_by_placeholder("yourname@hospital.com")
        self.first_name_input = self.page.get_by_placeholder("First name")
        self.last_name_input = self.page.get_by_placeholder("Last name")
        self.terms_of_use_checkbox = self.page.locator(
            "myt-checkbox", has_text="By ticking this box"
        )
        self.receive_emails_checkbox = self.page.locator(
            "myt-checkbox", has_text="I agree to receiving"
        )
        self.next_verification_btn = self.page.locator("myt-button").filter(
            has_text="Next: verification"
        )
        self.back_btn = self.page.locator("myt-button").filter(has_text="Back")

    @allure.step("Fill in sign up form")
    def create_account(self, email: str, first_name: str, last_name: str):
        """Fill in sign up form"""
        with allure.step(f"Fill in email: {email}"):
            self.email_input.fill(email)
            self.confirm_email_input.fill(email)
        with allure.step(
            f"Fill in first name: {first_name} and last name: {last_name}"
        ):
            self.first_name_input.fill(first_name)
            self.last_name_input.fill(last_name)
        with allure.step("Check terms of use and receive emails checkboxes"):
            # this is not optimal
            self.terms_of_use_checkbox.click()
            self.receive_emails_checkbox.click()
        with allure.step("Click on Next: verification button"):
            self.next_verification_btn.click()
