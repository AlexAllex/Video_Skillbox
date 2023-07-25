
import  pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture()

def set_up_browser ():

    options = ChromeOptions()
    driver = Chrome(options=options)
    driver.get("https://skillbox.ru/")
    driver.quit()
    yield driver
    driver.quit()