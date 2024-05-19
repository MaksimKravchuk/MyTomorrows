from playwright.sync_api import Locator, Page


class HomePage:

    def __init__(self, page: Page):
        self.page = page
        self.create_account_btn = self.page.get_by_text("Create account")

    def account_btn(self, first_name: str, last_name: str) -> Locator:
        """Get account button by first and last name"""
        return self.page.get_by_role("button", name=first_name + " " + last_name)
