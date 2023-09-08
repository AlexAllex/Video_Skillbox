#pytest_plugins = [
    #"Src.browser"
#]


#def pytest_addoption(parser):
    #parser.addini("selenium_url", "Selenium hub url")
    #parser.addini("browser_name", "Browser name for tests")
    #parser.addini("browser_version", "Browser version for tests")
    #parser.addini("headless", "Run browser in headless mode")

import  pytest
import webdriver_manager
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager






@pytest.fixture()

def set_up_browser ():

    options = ChromeOptions()
    driver = Chrome(options=options)
    options.page_load_strategy = "normal"
    #driver.get("https://skillbox.ru/")
    #driver.implicitly_wait(30)
    yield driver
    driver.quit()

#def set_up_brower()
    #options = Options()
    #options.page_load_strategy = "normal" #(здесь можно выставить none or eager)
    #driver = Remote(desired_capabilities={"browerName": "chrome", "browserVersion": "Latest"},
                    #command_executor="http://127.0.0.0:4444/wd/hub")
    #options = Options
    #driver.quit()
    #yield driver
@pytest.fixture()


def set_up_browser_1():



    driver = webdriver.Chrome()

    driver.set_window_size(1024, 600)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def set_up_browser_2():
    options = Options
    driver = webdriver.Chrome()

    options = ChromeOptions()
    #driver = Chrome(options=options)
    options.page_load_strategy = "normal"
    #driver.get("https://skillbox.ru/")
    #driver.implicitly_wait(30)
    yield driver
    driver.quit()