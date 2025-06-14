import pytest
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup")
class TestLogin:


    def test_login(self):
        # This line creates an instance of the LoginPage class, and passes the WebDriver instance (self.driver) to it.
        login_page = LoginPage(self.driver)
        login_page.login("Dhiya", "&pass23")
        # assert "Welcome" in login_page.message()

