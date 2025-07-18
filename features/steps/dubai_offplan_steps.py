from behave import Given, When, Then

@Then('enter minimum_price')
def enter_minimum_price(context):
    context.app.dubai_off_plan_page.enter_minimum_price()

@Then('enter maximum_price')
def enter_maximum_price(context):
    context.app.dubai_off_plan_page.enter_maximum_price()  # Fixed method name

@Then('click on the show_results_btn')
def click_show_results_button(context):
    context.app.dubai_off_plan_page.click_show_results_button()

