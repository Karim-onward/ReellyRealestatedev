from behave import given, when, then





@given ('open the main page')
def open_main_page(context):
    context.app.home_page.open()

@when ('login to the page')
def login(context):
    context.app.home_page.login()
