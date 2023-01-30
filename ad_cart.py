from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def ad_cart(driver):
    
    # driver = webdriver.Chrome()
    
    driver.find_element_by_css_selector(".a-button-text.a-declarative").click()
    sorts = driver.find_elements_by_css_selector(".a-dropdown-link")
    
    for i in sorts:
        if i.text == "Price: Low to High":
            i.click()
            break
        
    time.sleep(2)
    
    driver.find_element_by_css_selector(".a-icon.a-icon-star-medium.a-star-medium-4").click()
    
    time.sleep(2)
    
    driver.find_elements_by_css_selector(".a-size-medium.a-color-base.a-text-normal")[0].click()
    
    time.sleep(2)
    
    driver.find_elements_by_css_selector(".a-button-input")[0].click()
    
    time.sleep(1)
    
   
    
    
    
    
    