import pytest
from Utils.webdriver import open_close_browser
from POMS.Pages.HomePage import HomePageClass
from POMS.Pages.ArticlePage import ArticlePageClass


@pytest.mark.usefixtures("open_close_browser")
class Test:
    @pytest.mark.parametrize("name",
                             [
                                 "Nikola Tesla",
                                 "Henri Coanda",
                                 "Pythagoras"]
                             )
    def test_search_pesonality(self, name):

        homePage = HomePageClass(self.driver)
        # Search for a personality
        homePage.wikipedia_search(search_value=name)
        articlePage = ArticlePageClass(self.driver)
        # Print and Test data for birth and death
        articlePage.print_born_data("Born")
        articlePage.print_death_data("Died")
        articlePage.check_born_data("Born")
        articlePage.check_death_data("Died")
        # GO back to wikipedia land page
        self.driver.back()
