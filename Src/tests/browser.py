
import  pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options


@pytest.fixture()

def set_up_browser ():

    options = ChromeOptions()
    driver = Chrome(options=options)
    options.page_load_strategy = "normal"
    driver.get("https://skillbox.ru/")
    #driver.implicitly_wait(30)
    yield driver
    driver.quit()

#def set_up_brower()
    #options = Options()
    #options.page_load_strategy = "normal" #(здесь можно выставить none or eager)
    #driver = Remote(desired_capabilities={"browerName": "chrome", "browserVersion": "Latest"},
                    command_executor="http://127.0.0.0:4444/wd/hub")
    #options = Options
    #driver.quit()
    #yield driver
