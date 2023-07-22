#pytest_plugins = [
  #  "Src.browser"
#]
import  pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def set_up_browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


#@pytest.fixture()

#def set_up_browser ():

    #options = ChromeOptions()
    #driver = Chrome(options=options)
    #driver.get("https://skillbox.ru/")
    #driver.quit()
    #yield driver
    #driver.quit()