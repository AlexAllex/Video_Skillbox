from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions
import pytest
#import allure



class TestExample:
    def test_example(self):


        options = ChromeOptions()
        options.binary_location = r'C:/chromium-48/chrome.exe' #тут указываете ссылку на ваш хром браузер на вашем компьютере -Что это? Ссылка на хромдрайвер? /Users/aslanidialexandra/miniconda/envs/skillbox_3/lib/python3.11/site-packages/chromedriver_binary
        driver = Chrome(options=options)
        driver.get("https://skillbox.ru/")
        assert 'Skillbox – образовательная платформа с онлайн-курсами.' == driver.title





    def test_url(self):
        pass

    def test_context(self):
        pass







