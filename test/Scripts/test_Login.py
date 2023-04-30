import time
from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.LoginPage import LogiPage


class Test_Logis(WebDriverSetup):

    def test_Login_Fail(self):
        driver = self.driver
        self.driver.get(LogiPage.get_base_url())
        login_page = LogiPage(driver)
        time.sleep(3)
        login_page.sign_up("standard_user", "secret_sauce")
        login_page.click_sing_up()

    def test_Login_Success(self):
        driver = self.driver
        self.driver.get(LogiPage.get_base_url())
        login_page = LogiPage(driver)
        time.sleep(3)
        login_page.sign_up("Andres", "secret_sauce")
        login_page.click_sing_up()

