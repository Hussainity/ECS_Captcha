from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import *
from time import sleep

# Set Up
PATH = "C:/Users/hussa/Documents/chromedriver.exe"
driver = webdriver.Chrome(PATH)

# TODO: replace with toplist urls
urls = ["https://www.facebook.com"]

urls_no_login = []

for url in urls:

    # get website
    driver.get(url)
    sleep(1) 

    # find sign in
    count = 1 # set this to the number of ways we are looking for the log in button
    while (count >= 0):
        try:
            if (count == 4): x = driver.find_element(By.XPATH, "//*[text()='sign in']"); break
            if (count == 3): x = driver.find_element(By.XPATH, "//*[text()='log in']"); break
            if (count == 2): x = driver.find_element(By.XPATH, "//*[text()='Sign In']"); break
            if (count == 1): x = driver.find_element(By.XPATH, "//*[text()='Log In']"); break
            if (count == 0): urls_no_login.append(url); break # no log in found
                
        except Exception as e:
            count += 1

    x.click()
    # At this point, bot should be at login page... now look for username box

    break
    count = 1 # set this to the number of ways we are looking for the log in button
    while (count >= 0):
        try:
            if (count == 1):
                print()

            if (count == 0):
                # report that log in button not found, save it to log
                urls_no_login.append(url)
                break

        except Exception as e:
            count += 1


    # x = driver.find_element(By.XPATH, "//*[text()='Sign in']")
    x = driver.find_element(By.XPATH, "//*[text()='Log In']")
    x.click()
    sleep(2) 

    # find username password input boxes
    # driver.find_element(By.ID, "login-username").send_keys("hotdog@hotdog.com" + Keys.ENTER)
    # x = driver.find_element(By.ID, "identifierId")
    x = driver.find_element(By.ID, "email")
    x.send_keys("hotdog@hotdog.com")
    x = driver.find_element(By.ID, "pass")
    x.send_keys("SUHSUHSUH1!" + Keys.ENTER)
    sleep(2) 

    # grab source code, dump to url
    source_code = driver.page_source
    #with open(url[12:-4] + "_source.html", "w", encoding="utf-8") as f:
        #f.write(source_code)

    # grab screen shot, save it
    # driver.get_screenshot_as_file(url[12:-4] + "_screenshot.png")

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