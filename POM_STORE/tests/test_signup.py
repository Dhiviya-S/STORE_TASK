import pytest
from pages.Signup_page import SignupPage


@pytest.mark.usefixtures("setup")
class TestSignup:

    def test_signup(self):
        signup_page = SignupPage(self.driver)
        signup_page.signup("Dhiya", "&pass23")
        assert True

