from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions
import pytest
import allure

@allure.step("Проверка заголовка страницы")
def check_title(driver, title):
    assert title == driver.title





class TestExample:
   # def test_example(self):
       # options = ChromeOptions()
        #driver = Chrome(options=options)
        #driver.get("https://skillbox.ru/")
        #assert 'Skillbox – образовательная платформа с онлайн-курсами.' == driver.title



    def test_example(self, set_up_browser):
        driver = set_up_browser
        #driver.get("https://skillbox.ru")
        assert  'Skillbox - образовательная платформа с онлайн-курсами.' == driver.title
        check_title(driver=driver, title="Skillbox - образовательная платформа с онлайн-курсами")






