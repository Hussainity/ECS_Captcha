from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import *
from time import sleep

PATH = "C:/Users/hussa/Documents/chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://www.facebook.com")

sleep(1) 

x = driver.find_element(By.XPATH, "//*[text()='Sign in']")
x.click()

# x = driver.find_element(By.XPATH, "//*[ID()='Sign in']")

sleep(2) 

# driver.find_element(By.ID, "login-username").send_keys("hotdog@hotdog.com" + Keys.ENTER)

driver.find_element(By.ID, "identifierId").send_keys("hotdog@hotdog.com" + Keys.ENTER)

sleep(2) 

source_code = driver.page_source

with open("dump.txt", "w", encoding="utf-8") as f:
    f.write(source_code)

print(source_code.find("recaptcha"))

#driver.send_keys("")

# driver.close()




'''
1. have a list of URLs want to access alexa top 50

2. search the page for a sign in link, click on it
 -> try different casing/phrasing of this

3. search the page for username and password slots, put in info, hit enter/ find submit
 -> autocomplete tag? 

4. grab the source code after the attempt, take a screenshot and save it, take the source code and save it,

...

 1. search for recaptcha string and update some dictionary to keep track as you traverse through source code

'''