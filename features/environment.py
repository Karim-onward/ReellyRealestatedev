from selenium import webdriver
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.remote.remote_connection import ClientConfig
from app.application import Application


# Command to run tests with Allure & Behave:
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/target_search.feature

#Command to generate allure test report
#allure serve test_results/

def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """

    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    driver_path = GeckoDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Firefox(service=service)


    # context.driver.maximize_window()
    # context.driver.implicitly_wait(4)
    # context.app = Application(context.driver)

    # # HEADLESS MODE ####
    options = webdriver.FirefoxOptions()
    options.add_argument('headless')
    service = Service(GeckoDriverManager().install())
    context.driver = webdriver.Firefox(service=service


    )

    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service




    ## BROWSERSTACK ###
    #Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # client_config = ClientConfig(remote_server_addr="hub-cloud.browserstack.com")

    # bs_user = "afeez_5VNXrv"
    # bs_key = "o9cPtfUPjgh26j39nGm1"
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # #remote_url = "https://hub-cloud.browserstack.com/wd/hub"
    #
    #
    # options = Options()
    # bstack_options = {
    #     "os" : "Windows",
    #     "osVersion" : "11",
    #      'browserName': 'Edge',
    #     'browserVersion': 'latest',
    #      'sessionName': scenario_name,
    #  }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options,)


    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app=Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context. driver.quit()
