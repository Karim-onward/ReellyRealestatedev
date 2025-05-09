from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep



class DashboardPage(BasePage):
    #SETTING_BTN = (By.XPATH, "//a[@href='/settings']")
    SETTING_BTN = (By.XPATH, "//div[@class='settings-code w-embed']")


    def click_setting_btn(self):
        """Clicks the settings button on the dashboard."""
        self.click(*self.SETTING_BTN)
        sleep(3)



















