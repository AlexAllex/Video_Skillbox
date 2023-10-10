from  selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time
from selenium.webdriver.support.ui import Select
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

#from Src.tests.browser import set_up_browser_1


class TestGitHab1:
    
    @pytest.mark.keys_1
    def test_keys_1(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://github.com/microsoft/vscode/issues')
        #time.sleep(10)
        driver.find_element(By.CSS_SELECTOR, '.header-search-button.placeholder.input-button.form-control ').click()
        el = driver.find_element(By.ID, 'query-builder-test')
        el.send_keys('in:title')
        el.click()
        actions_chains = webdriver.ActionChains(driver)
        actions_chains.key_down(Keys.SPACE).click()
        el.send_keys('bug')
        el.click()
        find_elements = driver.find_elements(By.PARTIAL_LINK_TEXT, 'bug' or 'Bug')
        for i in find_elements: 
      
            assert "bug" or "Bug"in i.text , 'ссылка не содержит нужного слова'
        
       
    @pytest.mark.keys_2
    def test_keys_2(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://github.com/microsoft/vscode/issues')
        
        driver.find_element(By.CSS_SELECTOR, 'summary[title="Author"]').click()
        
        el1 = driver.find_element(By.ID, 'author-filter-field')
        el1.send_keys('bpasero')
        time.sleep(5)
        
        driver.find_element(By.XPATH, "//a/*[contains(text(), 'bpasero')]").click()
        #el1 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, "author-filter-field"))).click()
        
        
        time.sleep(10)
        Find_elements = driver.find_elements(By.PARTIAL_LINK_TEXT, 'bpasero')
        
        time.sleep(5)
       
        for i in Find_elements:
             print(i.text)
            
             assert "bpasero" in i.text, 'ссылка не содержит нужного слова'
          
        pass
    
    @pytest.mark.keys_3
    def test_keys_3(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://github.com/search/advanced')
        #time.sleep(10)
        driver.find_element(By.ID, "search_language").click()
        select = Select(driver.find_element(By.TAG_NAME, "select"))
        select.select_by_visible_text("Python")
        el1 = driver.find_element(By.ID, 'search_stars')
        el1.send_keys('>20000')
        el2 = driver.find_element(By.ID, 'search_filename')
        el2.send_keys('environment.yml')
        driver.find_element(By.CSS_SELECTOR, ".form-group.flattened .btn.flex-auto").click()
        find_elements = driver.find_elements(By.PARTIAL_LINK_TEXT, '>20k')
        for i in find_elements:
            assert '>20k' in i.text, 'ссылка не содержит нужного колличества звезд'
        pass
    
    @pytest.mark.keys_4
    def test_keys_4(self, set_up_browser_1):
        driver = set_up_browser_1
        driver.get("https://skillbox.ru/code/")
        time.sleep(10)
        driver.execute_script("window.scrollBy(0, 300);")
        driver.find_element(By.CSS_SELECTOR, "label[value='profession']").click()
        #time.sleep(5)
        first_slider = driver.find_element(By.XPATH,
                                           '//div[@aria-valuenow="1"]//button[@aria-label="Изменить диапозон"]')
        time.sleep(3)
        second_slider = driver.find_element(By.XPATH,
                                            '//div[@aria-valuenow="24"]//button[@aria-label="Изменить диапозон"]')
        action_chains = webdriver.ActionChains(driver)
        action_chains.click_and_hold(first_slider).move_by_offset(xoffset=80, yoffset=0).perform()
        action_chains.release().perform()
        action_chains.click_and_hold(second_slider).move_by_offset(xoffset=-60, yoffset=0).perform()
        action_chains.release().perform()

       

        driver.find_element(By.XPATH, "//span[contains(@class, 'filter-checkboxes-list__value')][1]").click()
        check_box = driver.find_element(By.XPATH, '//span[contains(@class, "filter-checkboxes-list__value")][1]')
        print('-'*20)
        print(check_box)

        print('-'*20)
        #assert check_box.is_selected(),  False
        time.sleep(5)
        
        card_list = driver.find_elements(By.XPATH, '//*[@class="ui-product-card"]//h3')
        print (card_list)
        #title_list = [card.title for card in card_list]
        #assert '1C' in title_list, 'Текст не присутсвует в заголовке'
        time.sleep(3)
        for title in card_list:
             print(title.text)
            
             #assert '1C' in title.iner_text(), 'Текст не присутсвует в заголовке'
             assert '1С' in title.text, 'Текст не присутсвует в заголовке'
      
        pass



    @pytest.mark.keys_5
    def test_keys_5(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://github.com/microsoft/vscode/graphs/commit-activity")
        time.sleep(13)
        table_column = driver.find_element(By.XPATH, "//*[@class='bar mini'][13]")
        action_chains = webdriver.ActionChains(driver)
        action_chains.move_to_element(table_column).perform()
        tultip_list = driver.find_elements(By.XPATH, '//div[@class="svg-tip n"]')

        for i in tultip_list:
            assert '263 commits the week of Dec 11' == i.text, 'Тултип не совпадает'
            
            
    def test_mouse_move(self, set_up_browser):
        with allure.step('Открытие страницы https://github.com/microsoft/vscode/graphs/commit-activity'):
            set_up_browser.get('https://github.com/microsoft/vscode/graphs/commit-activity')
        time.sleep(2)  # ожидание загрузки таблицы

        with allure.step('Наведение мышки на 13 элемент от начала графика'):
            table_column = set_up_browser.find_element(By.XPATH, "//*[@class='bar mini'][13]")
            action_chains = webdriver.ActionChains(set_up_browser)
            action_chains.move_to_element(table_column).perform()

        with allure.step('Проверка совпадения подсказки на графике с ожидаемым значением'):
            tultip_list = set_up_browser.find_elements(By.XPATH, '//div[@class="svg-tip n"]')
            for i in tultip_list:
                assert '294 commits the week of Nov 13' == i.text, 'Тултип не совпадает'
        pass
        
       
        
        
        

