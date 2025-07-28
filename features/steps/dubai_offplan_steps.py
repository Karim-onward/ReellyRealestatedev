from behave import Given, When, Then

@Then('enter minimum price {minimum_price}')
def enter_minimum_price(context, minimum_price):
    context.app.dubai_off_plan_page.enter_minimum_price(minimum_price)

@Then('enter maximum price {maximum_price}')
def enter_maximum_price(context, maximum_price):
    context.app.dubai_off_plan_page.enter_maximum_price(maximum_price)  # Fixed method name

@Then('click on the show_results_btn')
def click_show_results_button(context):
    context.app.dubai_off_plan_page.click_show_results_button()

# @Then('verify the price {price}')
# def verify_the_price(context, price):
#     context.app.dubai_off_plan_page.Verify_the_price()