from selenium import webdriver
import time


def scrape(driver):
    
    products = driver.find_elements_by_css_selector(".a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal")
    string = ""
    pr_list = []
    for i in range(0,20):
        
        if "$" in products[i].text:
            continue
        
        else:
            product = f"{products[i].text}\n"
            pr_list.append(product)
        
        
    for i in range(0,10):
        string += f"{i+1}. {pr_list[i]}"
            
    return string
        


    