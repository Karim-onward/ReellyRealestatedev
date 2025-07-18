from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep



class DubaiOffPlanPage(BasePage):
    INPUT_MINIMUM_PRICE = (By.CSS_SELECTOR, "input[name='priceMin']")
    INPUT_MAXIMUM_PRICE = (By.XPATH, "//input[@name='priceMax']")
    SHOW_RESULTS_BTN =(By.XPATH, "//button[@type='submit']")

    def enter_minimum_price(self):
        self.input_text("1200000", *self.INPUT_MINIMUM_PRICE)
        sleep(1)


    def enter_maximum_price(self):
        self.input_text("20000000", *self.INPUT_MAXIMUM_PRICE)
        sleep(1)

    def click_show_results_button(self):
        self.click(*self.SHOW_RESULTS_BTN)
        sleep(5)

