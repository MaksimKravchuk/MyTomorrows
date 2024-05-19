import allure

from pages.shared_elements import MaterialSelectorOverlay


class SetUpAccountPage:

    def __init__(self, page):
        self.page = page
        self.job_title_selector = MaterialSelectorOverlay(self.page, "Job title")
        self.speciality_selector = MaterialSelectorOverlay(self.page, "Speciality")
        self.country_selector = MaterialSelectorOverlay(self.page, "Country")
        self.registration_number_input = self.page.locator(
            "myt-input", has_text="HCP registration number"
        ).locator("input")
        self.complete_setup_btn = self.page.get_by_role("button", name="Complete setup")

        # I am involved in running clinical trials *
        self.is_running_clinical_trials_yes_btn = self.page.locator(
            "mat-radio-button", has_text="Yes"
        )
        self.is_running_clinical_trials_no_btn = self.page.locator(
            "mat-radio-button", has_text="No"
        )

    @allure.step("Setup account")
    def setup_account(
        self,
        job_title: str,
        specialty: str,
        country: str,
        registration_number: str,
        is_running_clinical_trials: bool,
    ):
        self.job_title_selector.select_option(job_title)
        self.speciality_selector.select_option(specialty)
        self.country_selector.select_option(country)
        with allure.step(f"Fill in registration number: {registration_number}"):
            self.registration_number_input.fill(registration_number)
        with allure.step(
            f"Select if user is running clinical trials: {is_running_clinical_trials}"
        ):
            if is_running_clinical_trials:
                self.is_running_clinical_trials_yes_btn.click()
            else:
                self.is_running_clinical_trials_no_btn.click()
        with allure.step("Click on Complete setup button"):
            self.complete_setup_btn.click()
