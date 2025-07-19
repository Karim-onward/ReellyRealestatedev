from behave import given, when, then





#@given ('open the main page')
#def open_main_page(context):
    #context.app.home_page.open_main_page()

#@when ('login to the page')
#def login(context):
    #context.app.home_page.login()



@given("the user is on the main page")
def open_main_page(context):
    """

    :param context:
    """
    context.app.home_page.open()

@when("the user logs into the page")
def login(context):
    """

    :param context:
    """
    context.app.home_page.login()