import unittest
from selenium import webdriver
import urllib3
from selenium.webdriver.chrome.service import Service


class WebDriverSetup(unittest.TestCase):
    def setUp(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        driver_service=Service(executable_path="C:\\Users\\brayan.piedrahita\\Desktop\\Automatizacion\\GPT\\test\\chromedriver.exe")
        driver = webdriver.Chrome(service=driver_service)
        self.driver = driver
        self.driver.maximize_window()

    def tearDown(self):
        if self.driver is not None:
            self.driver.close()
            self.driver.quit()