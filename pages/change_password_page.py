from selenium.webdriver.common.by import By
from pages.base_page import BasePage



class ChangePasswordPage(BasePage):

    #VerifyChangePasswordPage = (By.XPATH,"//div[@class='change-password-text']")
    EnterNewPassword = (By.XPATH, "//input[@data-name='Enter new password']")
    RepeatPassword = (By.XPATH, "//input[@data-name='Repeat password']")
    VerifyChangePassword = (By.XPATH,"//a[@class='submit-button-2 w-button']")


    def enter_new_password(self, password):
        self.input_text('drinkwater',  *self.EnterNewPassword)
        self.input_text('drinkwater', *self.RepeatPassword)

    def verify_change_password_button(self):
        return self.find_element(*self.VerifyChangePassword).is_displayed()







