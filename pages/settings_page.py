from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep





class SettingsPage(BasePage):

    CHANGE_PASSWORD_BUTTON = (By.XPATH, "//a[@href='/set-new-password']")

    def click_change_password_button(self):
        """Clicks the change password button on the dashboard."""
        self.click(*self.CHANGE_PASSWORD_BUTTON)
        sleep(3)


