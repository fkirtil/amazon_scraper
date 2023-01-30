from selenium import webdriver
import login, find, scrape, write, ad_cart, signout, time


driver = webdriver.Chrome()


credentials = {"email": 'iremsmail4@gmail.com', "password": 'SeZdbj(aR32*U,.'}


login.login(credentials, driver)
find.find("Noise Cancelation headphones" , driver)
products = scrape.scrape(driver)
write.write(products, "ÜrünListesi.txt")
print(products)

ad_cart.ad_cart(driver)

signout.signout(driver)
time.sleep(5)
driver.close()




    
        

                
