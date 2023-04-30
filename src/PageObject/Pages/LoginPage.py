import time

from selenium.webdriver.common.by import By

base_url = "https://www.saucedemo.com/"


class LogiPage:
    def __init__(self, driver):
        self.driver = driver
        self.user = "user-name"
        self.password = "password"
        self.submit_button = "login-button"

    def get_user_name(self):
        return self.driver.find_element(By.ID, self.user)

    def get_user_password(self):
        return self.driver.find_element(By.ID, self.password)

    def get_submit_button(self):
        return self.driver.find_element(By.ID, self.submit_button)

    def sign_up(self, user, password):
        self.get_user_name().send_keys(user)
        self.get_user_password().send_keys(password)
        time.sleep(3)

    def click_sing_up(self):
        self.get_submit_button().click()
        time.sleep(3)

    @staticmethod
    def get_base_url():
        return base_url