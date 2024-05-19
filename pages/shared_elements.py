import allure


class MaterialSelectorOverlay:

    # Probably not an optimal solution, but it's a good start

    def __init__(self, page, header: str):
        self.page = page
        self.header = header
        self.base_selector = self.page.locator(".myt-select", has_text=header)
        self.dropdown_btn = self.base_selector.locator("mat-form-field")
        self.list_base_locator = self.page.locator(".cdk-overlay-container").get_by_role(
            "listbox")  # It's better to have a more specific selector

    def select_option(self, option: str):
        with allure.step(f"Select option {option} for {self.header}"):
            self.dropdown_btn.click()
            return self.list_base_locator.locator("mat-option").filter(has_text=option).click()
