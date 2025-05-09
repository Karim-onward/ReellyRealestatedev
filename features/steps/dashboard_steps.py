from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from behave import Given, When, Then




@When ('click on the setting_btn at the right side')
def click_setting_button(context):
    context.app.dashboard_page.click_setting_btn()

