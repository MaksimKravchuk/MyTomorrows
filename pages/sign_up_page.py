from playwright.sync_api import Page


class SignUpPage:
    def __init__(self, page: Page):
        self.page = page
        self.create_account_btn = self.page.get_by_role("button", name="Create account")
