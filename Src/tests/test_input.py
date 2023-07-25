from  selenium import  webdriver
from selenium.webdriver import  Keys
from selenium.webdriver.common.by import By
import time


class TestInput:
    def test_send_keys(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://l6nm9r.csb.app/demo/InputTextDemo.html")
        driver.find_element(By.ID, "username1").send_keys('basic text')


    def test_clear(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://l6nm9r.csb.app/demo/InputTextDemo.html")
        el =driver.find_element(By.ID, "username1")
        el.send_keys("basic text")
        el.clear()  #отчистить поле


    def test_copy_paste(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://l6nm9r.csb.app/demo/InputTextDemo.html")
        time.sleep(20)
        el = driver.find_element(By.ID, "username1")
        el.send_keys("basic text")
        action_chains = webdriver.ActionChains(driver)
        action_chains.key_down(Keys.COMMAND).send_keys('c').perform() # выделить текст сочетанием клавиш cm+c
        el.clear()
        el.click()
        action_chains.key_down(Keys.COMMAND).send_keys("v").perform() # вставить выделенный текст сочетанием клавиш cm+v


    def test_input_mask(self, set_up_browser): # введение маск
        driver = set_up_browser
        driver.get("https://jbms5d.csb.app/demo/InputMaskDemo.html")
        time.sleep(20)
        el = driver.find_element(By.ID, "basic")
        value = '12345678'
        for c in value:
            el.send_keys(c)
            time.sleep(0.2)

    def test_input_filter(self, set_up_browser):  # проверка что цифры не вводяться в поле
            driver = set_up_browser
            driver.get("https://yypr78.csb.app/demo/InputFilterDemo.html")
            driver.find_element(By.ID, "alpha").send_keys('asd123qwe321')

    def test_input_tag(self, set_up_browser):  # проверка что можно ввести тег в поле специальное
        driver = set_up_browser
        driver.get("https://esy8bz.csb.app/demo/ChipsDemo.html")
        driver.find_element(By.XPATH, "(//input)[3]").send_keys('skillbox') + Keys.ENTER
        pass










