from POMS.Pages.BaseClass import BaseClass
from selenium.webdriver.common.by import By
from selenium.common import exceptions as SelExc
import pytest
import re

birthDates = ['7 June 1886','570 BC','10 July 1856']
deathDates = ['495 BC','25 November 1972','7 January 1943']

class ArticlePageClass(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)

    def get_value_in_table(self, table_element, header_text):
        row_elements = table_element.find_elements(By.TAG_NAME, "tr")
        for row in row_elements:
            try:
                h = row.find_element(By.TAG_NAME, "th").text.strip()
            except SelExc.NoSuchElementException:
                h = ''

            if header_text in h:
                try:
                    d = row.find_element(By.TAG_NAME, "td").text.strip()
                except SelExc.NoSuchElementException:
                    d = None
                return d

        return None  # header text was not found

    def get_value_from_infobox(self, header_text):
        i = self.driver.find_element(By.CSS_SELECTOR, 'table.infobox')
        return self.get_value_in_table(i, header_text)

    def print_born_data(self, section):
        born_content = self.get_value_from_infobox(section)
        print(f"\n{born_content}")
        return born_content

    def print_death_data(self, section):
        died_content = self.get_value_from_infobox(section)
        print(f"\n{died_content}")
        return died_content

    def check_born_data(self,section):
        born_content = self.get_value_from_infobox(section)
        birthdate = re.search('\d{1,2} [a-zA-Z]+ \d{4}', born_content)
        if birthdate is None:
            pytest.fail("data not very precise")
        else:
            if birthdate.group(0) not in birthDates:
                pytest.fail(f"birthday is not accurate on Wikipedia")

    def check_death_data(self,section):
        died_content = self.get_value_from_infobox(section)
        deathDate = re.search('\d{1,2} [a-zA-Z]+ \d{4}', died_content)
        if deathDate is None:
            pytest.fail("data not very precise")
        else:
            if deathDate.group(0) not in deathDates:
                pytest.fail(f"death date is not accurate on Wikipedia")