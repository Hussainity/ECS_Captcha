from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import *
from time import sleep

# Set Up
PATH = "C:/Users/hussa/Documents/chromedriver.exe"
driver = webdriver.Chrome(PATH)

# TODO: replace with toplist urls
urls = ["https://www.yahoo.com"]

urls_no_login = []

for url in urls:

    # get website
    driver.get(url)
    sleep(1) 

    # find sign in
    count = 7 # set this to the number of ways we are looking for the log in button
    while (count >= 0):
        try:
            # KORI: Follow this pattern to add new lines to find the log in button
            if (count == 7): driver.find_element(By.XPATH, "//*[text()='sign in']").click(); break
            if (count == 6): driver.find_element(By.XPATH, "//*[text()='log in']").click(); break
            if (count == 5): driver.find_element(By.XPATH, "//*[text()='Sign In']").click(); break
            if (count == 4): driver.find_element(By.XPATH, "//*[text()='Log In']").click(); break
            if (count == 3): driver.find_element(By.XPATH, "//*[text()='Sign in']").click(); break
            if (count == 2): x = driver.find_element(By.XPATH, "//*[text()='Log in']").click(); break
            if (count == 1):
                driver.get(url + "/login")
                break
            if (count == 0):
                 urls_no_login.append(url); break # no log in found
                
        except Exception as e:
            count -= 1

    # At this point, bot should be at login page... now look for username box
    sleep(1)

    count = 5 # set this to the number of ways we are looking for the log in button
    while (count >= 0):
        try:

            x = None

            # KORI: Follow this pattern to add new lines to find the user name box
            if (count == 4): x = driver.find_element(By.ID, "user")
            if (count == 3): x = driver.find_element(By.ID, "login-username")
            if (count == 2): x = driver.find_element(By.ID, "username")
            if (count == 1): x = driver.find_element(By.ID, "email")
            if (count == 0):
                print("no username found in login page")
                break

            x.send_keys("ece8803@hotmail.com")
            break

        except Exception as e:
            count -= 1


    print(urls_no_login)
    sleep(2)
    driver.close()
    break





### WORK BOX BELOW - IGNORE ###

'''


    # find username password input boxes
    # driver.find_element(By.ID, "login-username").send_keys("hotdog@hotdog.com" + Keys.ENTER)
    # 
    
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





1. have a list of URLs want to access alexa top 50

2. search the page for a sign in link, click on it
 -> try different casing/phrasing of this

3. search the page for username and password slots, put in info, hit enter/ find submit
 -> autocomplete tag? 

4. grab the source code after the attempt, take a screenshot and save it, take the source code and save it,

...

 1. search for recaptcha string and update some dictionary to keep track as you traverse through source code

'''