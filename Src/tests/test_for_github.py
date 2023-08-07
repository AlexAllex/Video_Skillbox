from  selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time
from selenium.webdriver.support.ui import Select

from Src.tests.browser import set_up_browser_1


class TestGitHab1:
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
       # expected_value = "Bug" or 'bug'
        #bug_name = driver.find_element(By.CSS_SELECTOR, ".Text-sc-17v1xeu-0.kWPXhV.search-match")


        #assert bug_name.get_attribute('class') == expected_value

    def test_keys_2(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://github.com/microsoft/vscode/issues')
        #time.sleep(10)
        driver.find_element(By.CSS_SELECTOR, '.btn-link[title="Author"] ').click()
        el1 = driver.find_element(By.ID, 'author-filter-field')
        el1.send_keys('bpasero')
        el1.click()
        #author = driver.find_element(By.CSS_SELECTOR, '.opened-by')
        #expected_value = " bpasero"

        #assert author.get_attribute('class') == expected_value
        #assert author.text == expected_value
        pass
    
    
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
         
        pass
    
    
    def test_keys_4(self, set_up_browser_1):
        driver = set_up_browser_1
        driver.get("https://skillbox.ru/code/")
        time.sleep(20)
        driver.execute_script("window.scrollBy(0, 300);")
        driver.find_element(By.CSS_SELECTOR, "label[value='profession']").click()
        time.sleep(10)
        first_slider = driver.find_element(By.XPATH,
                                           '//div[@aria-valuenow="1"]//button[@aria-label="Изменить диапозон"]')
        time.sleep(10)
        second_slider = driver.find_element(By.XPATH,
                                            '//div[@aria-valuenow="24"]//button[@aria-label="Изменить диапозон"]')
        action_chains = webdriver.ActionChains(driver)
        action_chains.click_and_hold(first_slider).move_by_offset(xoffset=80, yoffset=0).perform()
        action_chains.release().perform()
        action_chains.click_and_hold(second_slider).move_by_offset(xoffset=-60, yoffset=0).perform()
        action_chains.release().perform()


        driver.find_element(By.XPATH, "(//*[contains(@class, 'filter-checkboxes-list__value')])[5]").click()
        time.sleep(5)
        pass




    def test_keys_5(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://github.com/microsoft/vscode/graphs/commit-activity")
        time.sleep(13)
        action_chains = webdriver.ActionChains(driver)

        #action_chains.move_to_element( driver.find_element(By.CSS_SELECTOR, '.bar.mini.active'))\
           # .perform()
        table_column = driver.find_element(By.XPATH, "//*[@class='bar mini'][13]")
        action_chains = webdriver.ActionChains(driver)
        action_chains.move_to_element(table_column).perform()
        pass
        
       
        
        
        

