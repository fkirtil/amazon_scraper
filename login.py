from selenium import webdriver
import time

def login(credentials, driver):
    link = "https://www.amazon.com/"
    
    
    driver.get(link)
    
    driver.find_elements_by_css_selector(".nav-line-1.nav-progressive-content")[1].click()
    
    time.sleep(1)
    
    driver.find_element_by_id("ap_email").send_keys(credentials["email"])
    driver.find_element_by_css_selector(".a-button-input").click()
    
    time.sleep(1)
    
    driver.find_element_by_id("ap_password").send_keys(credentials["password"])
    driver.find_element_by_css_selector(".a-button-input").click()
    
    time.sleep(2)
    

    
    
