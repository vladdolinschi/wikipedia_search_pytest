from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BaseClass:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self,element_locator):
        """"
        Click on a desired element based on its locator while waiting 5s for it to be visible.
        """
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(element_locator)).click()

