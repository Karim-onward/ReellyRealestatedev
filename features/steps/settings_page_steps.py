from behave import Given, When, Then



@Then ('click on the change password button')
def click_change_password_button(context):
    context.app.settings_page.click_change_password_button()