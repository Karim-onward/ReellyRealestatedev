from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """Base class for all page objects, providing common Selenium actions."""

    def __init__(self, driver):
        """Initialize the base page with WebDriver and explicit wait."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_url(self, url):
        """Navigate to the specified URL."""
        self.driver.get(url)

    def click(self, *locator):
        """Click the element located by the given locator."""
        self.driver.find_element(*locator).click()

    def find_element(self, *locator):
        """Find and return a single web element."""
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        """Find and return a list of web elements."""
        return self.driver.find_elements(*locator)

    def input_text(self, text, *locator):
        """Enter text into an input field located by the given locator."""
        element = self.driver.find_element(*locator)
        element.send_keys(text)

    def wait_for_element_visible(self, *locator):
        """Wait for the element to be visible."""
        self.wait.until(
             EC.visibility_of_element_located(*locator),
             message=f'element {locator} not visible'
          )

    def wait_for_element_invisible(self, *locator):
        """Wait for the element to be visible."""
        self.wait.until(
            EC.invisibility_of_element_located(*locator),
            message=f'element {locator} should not be visible'
        )

    def wait_for_element_clickable(self, *locator):
        """Wait for the element to be clickable."""
        self.wait.until(
            EC.element_to_be_clickable(*locator),
            message=f'element {locator} not clickable'
        )

    def wait_and_click(self, *locator):
        """Wait for the element to be visible."""
        self.wait.until(
            EC.element_to_be_clickable(*locator),
            message=f'element {locator} not visible'
        ).click()


    def verify_current_url(self, expected_url):
        """Assert that the current URL matches the expected URL."""
        actual_url = self.driver.current_url
        assert actual_url == expected_url, f'Expected {expected_url} does not match {actual_url}'
    def verify_partial_text(self, expected_text, *locator):
        """Assert that the partial text matches the expected text."""
        actual_text = self.find_element(*locator).text
        assert actual_text == expected_text, f'Expected {expected_text} does not match {actual_text}'
    def verify_text(self, expected_text, *locator):
        """Assert that the text matches the expected text."""
        actual_text = self.find_element(*locator).text
        assert actual_text == expected_text, f'Expected {expected_text} but got {actual_text}'

    def partial_url(self, expected_url):
        """Find and return a partial URL."""
        actual_url = self.driver.current_url
        assert expected_url in actual_url, f'expected partial URL {expected_url} but got {actual_url}'
















