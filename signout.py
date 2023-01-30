from selenium import webdriver
from selenium.webdriver import ActionChains

import time


def signout(driver):
   
    actions = ActionChains(driver)
    
    menu = driver.find_elements_by_css_selector(".nav-line-1.nav-progressive-content")[1]
    actions.move_to_element(menu).perform()
    driver.find_element_by_id("nav-item-signout").click()
    