from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions
#from selenium.webdriver.chrome.options import Options
#from webdriver_manager.chrome import ChromeDriverManager
import pytest
#import allure



class TestExample:
    def test_example(self):


        options = ChromeOptions()
        options.binary_location = r'/Applications/Google/Chrome.app/Contents/MacOS/Google/Chrome 114'
        driver = Chrome(options=options)
        driver.get("https://skillbox.ru/")
        assert 'Skillbox – образовательная платформа с онлайн-курсами.' == driver.title
        
        from selenium import webdriver


    #driver = webdriver.Chrome(ChromeDriverManager().install())
    #driver.set_window_size(1024, 600)
    #driver.maximize_window()





    def test_url(self):
        pass

    def test_context(self):
        pass







