from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep


class HomePage(BasePage):

    INPUT_USERNAME = (By.XPATH, "//input[@wized='emailInput']")
    INPUT_PASSWORD = (By.XPATH, "//input[@wized='passwordInput']")
    LOGIN_BTN = (By.XPATH, "//a[@wized='loginButton']")


    def open(self):
        self.open_url('https://soft.reelly.io/sign-in')
        sleep(5)

    def login(self):
        self.input_text('afeezkareem179@yahoo.com',*self.INPUT_USERNAME)
        self.input_text('Walleboy@123',*self.INPUT_PASSWORD)
        self.click(*self.LOGIN_BTN)
        sleep(10)




