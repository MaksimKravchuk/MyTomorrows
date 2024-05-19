import allure
from playwright.sync_api import Page


class SetPasswordPage:

    def __init__(self, page: Page):
        self.page = page
        self.password_input = self.page.get_by_placeholder("Enter your password")
        self.confirm_password_input = self.page.get_by_placeholder(
            "Confirm your password"
        )
        self.activate_account_btn = self.page.get_by_role(
            "button", name="Activate account"
        )

    @allure.step("Set password")
    def set_password(self, password: str):
        """Set password"""
        self.password_input.fill(password)
        self.confirm_password_input.fill(password)
        self.activate_account_btn.click()
