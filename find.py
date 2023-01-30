from selenium import webdriver
import time


def find(category, driver):
    driver.get("https://www.amazon.com/")
    
    driver.find_elements_by_css_selector(".nav-input.nav-progressive-attribute")[0].send_keys(category)
    driver.find_elements_by_css_selector(".nav-input.nav-progressive-attribute")[1].click()
    
    time.sleep(1)
    
    
    #sort by price
    
    driver.find_element_by_css_selector(".a-button-text.a-declarative").click()
    sorts = driver.find_elements_by_css_selector(".a-dropdown-link")
    
    for i in sorts:
        if i.text == "Price: High to Low":
            i.click()
            break
        
    time.sleep(2)
        
        
    
    
    
    
    
    
    
    