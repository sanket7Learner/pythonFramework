from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from globalLocators import *


class SetUpDetails:
    @staticmethod
    def init_driver():
        driver = webdriver.Chrome("C:/Users/Sanket/Downloads/chromedriver_win32/chromedriver.exe")
        driver.set_page_load_timeout(30)
        driver.implicitly_wait(30)
        driver.maximize_window()
        return driver