from behave import Given, When, Then



@When ('click on the off_plan_button')
def click_off_plan_btn(context):
    context.app.off_plan_page.click_off_plan_button()

@When ('click on the filter_button')
def click_filter_button(context):
    context.app.off_plan_page.click_filter_btn()