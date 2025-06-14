from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    Login=(By.ID,"login2")
    USERNAME_INPUT = (By.ID,"loginusername")
    PASSWORD_INPUT = (By.ID,"loginpassword")
    LOGIN_BUTTON = (By.XPATH,"//button[@onclick='logIn()']")
    WELCOME = (By.XPATH, "//a[contains(text(),'Welcome')]")


    def login(self, username, password):
        self.click_element(self.Login)
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)

    def message(self):
       msg=self.find_element(self.WELCOME)
       return msg.text




