import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

chrome_path = "D:\Drivers\chromedriver.exe"
website_url = "https://www.wikipedia.org/"
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_path, options=chrome_options)


@pytest.fixture(scope="class")
def open_close_browser(request):

    driver.get(website_url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()
