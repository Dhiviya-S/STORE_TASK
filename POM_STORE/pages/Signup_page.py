from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SignupPage(BasePage):
    SIGNUP=(By.ID,"signin2")
    USERNAME_INPUT = (By.ID,"sign-username")
    PASSWORD_INPUT = (By.ID,"sign-password")
    SIGNUP_BUTTON = (By.XPATH,"//button[@onclick='register()']")

    def signup(self, username, password):
        self.click_element(self.SIGNUP)
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click_element(self.SIGNUP_BUTTON)


