from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.dubai_offplan_page import DubaiOffPlanPage
from pages.off_plan_page import OffPlanPage
#from pages.dashboard_page import DashboardPage
#from pages.change_password_page import
#from pages.settings_page import SettingsPage





class Application:
    def __init__(self, driver):
        self.driver = driver
        self.base_page = BasePage(self.driver)
        self.home_page = HomePage(self.driver)
        self.off_plan_page = OffPlanPage(self.driver)
        self.dubai_off_plan_page = DubaiOffPlanPage(self.driver)
        #self.change_password_page = (self.driver)
        #self.dashboard_page = DashboardPage(self.driver)
        # self.settings_page = SettingsPage(self.driver)

