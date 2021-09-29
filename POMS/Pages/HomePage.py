from selenium.webdriver.common.by import By
from POMS.Pages.BaseClass import BaseClass
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class HomePageClass(BaseClass):

    search_input_field = "searchInput"
    submit_search_button = "button.pure-button"
    infobox = (By.CSS_SELECTOR, 'table.infobox')

    def __init__(self, driver):
        super().__init__(driver)

    def get_page_title(self):
        return self.driver.title

    def wikipedia_search(self,search_value):
        """
        :param element_locator: locator of the elements that have the same css_selector
        :param search_value: string that will be searched
        :return:
        """
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.ID, f"{self.search_input_field}")))
        self.driver.find_element_by_id(self.search_input_field).send_keys(search_value)
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.CSS_SELECTOR, f"{self.submit_search_button}"))).click()

