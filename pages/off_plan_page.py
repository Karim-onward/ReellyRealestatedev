from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

class OffPlanPage(BasePage):
    OFF_PLAN_BTN = (By.XPATH, "//a[@wized='newOffPlanLink' and @class='menu-button-block w-inline-block']")
    VERIFY_OFF_PLAN_PAGE = (By.CSS_SELECTOR, ".flex.gap-4")
    FILTER_BTN = (By.XPATH, "//button[text()='Search & filters']")

    def click_off_plan_button(self):
        """Click the Off Plan sidebar button."""
        self.click(*self.OFF_PLAN_BTN)
        sleep(1)  # Consider replacing with WebDriverWait

    def verify_off_plan_page(self):
        """Verify the Off Plan page is displayed."""
        return self.find_element(*self.VERIFY_OFF_PLAN_PAGE).is_displayed()

    def click_filter_btn(self):
        """Click the Filter button on the Off Plan page."""
        self.click(*self.FILTER_BTN)
        sleep(5)  # Same here — WebDriverWait is better