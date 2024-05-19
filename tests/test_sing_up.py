import re

import allure
import pytest
from faker import Faker
from playwright.sync_api import Page, expect
from tempmail import EMail

from pages.crate_account_page import CreateAccountPage
from pages.home_page import HomePage
from pages.set_password_page import SetPasswordPage
from pages.setup_account_page import SetUpAccountPage
from pages.sign_up_page import SignUpPage


@pytest.fixture(autouse=True)
def fake() -> Faker:
    """Faker instance"""
    return Faker()


@pytest.fixture()
def email() -> EMail:
    """Temp mail instance"""
    email = EMail()
    return email


class TestSignUp:
    def test_user_can_sign_up(self, page: Page, email: EMail, fake: Faker):
        """Test user can sign up"""
        page.goto("/home")
        with allure.step("Click on Create account button on Home page"):
            home_page = HomePage(page)
            home_page.create_account_btn.click()

        with allure.step("Click on Create account button on Sign up page"):
            sign_up_page = SignUpPage(page)
            sign_up_page.create_account_btn.click()

        with allure.step("Sign up with email"):
            create_account_page = CreateAccountPage(page)
            first_name = fake.first_name()
            last_name = fake.last_name()
            create_account_page.create_account(
                email=email.address, first_name=first_name, last_name=last_name
            )

            with allure.step("Receive email with verification link"):
                msg = email.wait_for_message()
                pattern = re.compile(
                    r"""https://platform-develop.mytomorrows.com/create-account/set-password\?([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"""
                )  # this regex can be more universal
                match = re.search(pattern, msg.text_body)
                link = match.group(0)

        with allure.step("Open verification link"):
            page.goto(link)

        with allure.step("Fill in password"):
            set_password_page = SetPasswordPage(page)
            set_password_page.set_password("!Qwerty12345")

        setup_account_page = SetUpAccountPage(page)

        with page.expect_response("**/health-care-professional/**") as response_info:
            setup_account_page.setup_account(
                job_title="study director",
                specialty="Cardiology",
                country="Argentina",
                registration_number=fake.random_number(),
                is_running_clinical_trials=True,
            )
        response = response_info.value
        assert response.ok, f"Response {response.url} is not {response.status}. {response.text}"

        with allure.step("Check that user is logged in"):
            expect(home_page.account_btn(first_name, last_name)).to_be_visible()
