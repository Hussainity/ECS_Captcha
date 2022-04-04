from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import *
from time import sleep

# set up
PATH = "C:/Users/hussa/Documents/chromedriver.exe"
driver = webdriver.Chrome(PATH)

url = "https://www.google.com"

# get website
driver.get(url)
sleep(1) 

# find sign in
'''
1. look for sign in text
2. try accessing url.com/login
3. look for log in text
4. look for sign in by ID # x = driver.find_element(By.XPATH, "//*[ID()='Sign in']")
'''
x = driver.find_element(By.XPATH, "//*[text()='Sign in']")
x.click()
sleep(2) 

# find username password input boxes
    # driver.find_element(By.ID, "login-username").send_keys("hotdog@hotdog.com" + Keys.ENTER)
x = driver.find_element(By.ID, "identifierId")
x.send_keys("hotdog@hotdog.com" + Keys.ENTER)
sleep(2) 

# grab source code, dump to url
source_code = driver.page_source
with open(url[12:-4] + "_source.html", "w", encoding="utf-8") as f:
    f.write(source_code)
    
# grab screen shot, save it
driver.get_screenshot_as_file(url[12:-4] + "_screenshot.png")

print(source_code.find("recaptcha"))

#driver.send_keys("")

driver.close()




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