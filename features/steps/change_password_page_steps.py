from behave import Given, When, Then



#@Then ('Verify the right page opens')
#def verify_right_page(context):
    #context.app.change_password_page.verify_right_page()

@Then ('enter new password')
def enter_new_password(context):
    context.app.change_password_page.enter_new_password('drinkwater')

#@Then ('repeat password')
#def repeat_password(context):
    #context.app.change_password_page.repeat_password()

@Then ('verify change password button is displayed')
def verify_change_password_button(context):
    context.app.change_password_page.verify_change_password_button()

