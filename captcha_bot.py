from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import *
from time import sleep
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from collections import defaultdict

USERNAME = "hussain_miya@hotmail.com"
PASSWORD = "Password1!"

# Set Up
PATH = "C:/Users/hussa/Documents/chromedriver.exe"
#PATH = "C:/Users/korib/OneDrive - Georgia Institute of Technology/ECSproj/chromedriver.exe"
#driver = webdriver.Chrome(PATH)
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 1 
})
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(PATH, service=s, options=options)
driver.maximize_window()

# TODO: replace with toplist urls
urls = ["https://www.google.com","https://www.yahoo.com", "https://www.amazon.com", "https://www.reddit.com", "https://www.instagram.com", "https://en.wikipedia.org/wiki/Main_Page", "https://www.bing.com", "https://www.linkedin.com", "https://www.twitter.com", "https://www.zoom.us", "https://www.ebay.com", "https://www.office.com", "https://www.live.com",  "https://www.fandom.com/", "https://www.microsoft.com", "https://www.nytimes.com"]
# urls = ["https://www.reddit.com/login"]


records = defaultdict(dict)

'''
records:
    - url:
        - resolved: T/F
        - login:    code #
        - username: code #
        - password: code # 
'''

urls_found_signin_btn = 0
urls_no_login = []
urls_cannot_resolve = []

def find_username():
    count = 17 # set this to the number of ways we are looking for the log in button
    username_box = None
    while (count >= 0):
        try:
            if (count == 17):
                username_box = driver.find_element(By.XPATH, "//input[@type= 'email']")
                break
            if (count == 16):
                username_box = driver.find_element(By.XPATH, "//input[@id= 'user_login']")
                break
            if (count == 15):
                username_box = driver.find_element(By.XPATH, "//input[@name= 'log']")
                break
            if (count == 14):
                username_box = driver.find_element(By.XPATH, "//select[@autocomplete= 'email']")
                break
            if (count == 13):
                username_box = driver.find_element(By.XPATH, "//input[@autocomplete= 'email']")
                break
            if (count == 12):
                username_box = driver.find_element(By.XPATH, "//textarea[@autocomplete= 'email']")
                break
            if (count == 11):
                username_box = driver.find_element(By.XPATH, "//input[@type= 'email']")
                break
            if (count == 10):
                username_box = driver.find_element(By.XPATH, "//input[@name= 'Username']")
                break
            if (count == 9):
                username_box = driver.find_element(By.XPATH, "//input[@name= 'username']")
                break
            if (count == 8):
                username_box = driver.find_element(By.XPATH, "//input[@name= 'email']")
                break
            if (count == 7):
                username_box = driver.find_element(By.XPATH, "//select[@autocomplete= 'new-username']")
                break
            if (count == 6):
                username_box = driver.find_element(By.XPATH, "//input[@autocomplete= 'new-username']")
                break
            if (count == 5):
                username_box = driver.find_element(By.XPATH, "//textarea[@autocomplete= 'new-username']")
                break
            if (count == 4):
                username_box = driver.find_element(By.ID, "email")
                break
            if (count == 3):
                username_box = driver.find_element(By.XPATH, "//select[@autocomplete= 'username']")
                break
            if (count == 2):
                username_box = driver.find_element(By.XPATH, "//input[@autocomplete= 'username']")
                break
            if (count == 1):
                username_box = driver.find_element(By.XPATH, "//textarea[@autocomplete= 'username']")
                break
            if (count == 0):
                print(url + ": no username box found in login page")
                break
        except:
          # if just needs user--> send to keyboard and click enter if possible
            count -= 1
    return (username_box, count)

def find_password():
    
    # password find
    # ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/autocomplete and https://www.lambdatest.com/blog/locators-in-selenium-webdriver-with-examples/
    count = 10 # set this to the number of ways we are looking for the log in button
    password_box = None
    while (count >= 0):
        try:
            if (count == 10):
                password_box = driver.find_element(By.XPATH, "//input[@type= 'password']")
                password_box.send_keys(Keys.BACKSPACE)
                break
            if (count == 9):
                password_box = driver.find_element(By.XPATH, "//input[@id= 'loginPassword']")
                password_box.send_keys(Keys.BACKSPACE)
                break
            if (count == 8):
                password_box = driver.find_element(By.XPATH, "//select[@autocomplete= 'new-password']")
                password_box.send_keys(Keys.BACKSPACE)
                break
            if (count == 7):
                password_box = driver.find_element(By.XPATH, "//input[@autocomplete= 'new-password']")
                password_box.send_keys(Keys.BACKSPACE)
                break
            if (count == 6):
                password_box = driver.find_element(By.XPATH, "//textarea[@autocomplete= 'new-password']")
                password_box.send_keys(Keys.BACKSPACE)
                break
            if (count == 5):
                password_box = driver.find_element(By.XPATH, "//select[@autocomplete= 'current-password']")
                password_box.send_keys(Keys.BACKSPACE)
                break
            if (count == 4):
                password_box = driver.find_element(By.XPATH, "//input[@autocomplete= 'current-password']")
                password_box.send_keys(Keys.BACKSPACE)
                break
            if (count == 3):
                password_box = driver.find_element(By.XPATH, "//textarea[@autocomplete= 'current-password']")
                password_box.send_keys(Keys.BACKSPACE)
                break
            if (count == 2):
                password_box = driver.find_element(By.XPATH, "//input[@id= 'password']")
                password_box.send_keys(Keys.BACKSPACE)
                break
            if (count == 1):
                password_box = driver.find_element(By.XPATH, "//input[@name= 'password']")
                password_box.send_keys(Keys.BACKSPACE)
                break
            if (count == 0):
                print(url + ": no password box found in login page")
                break
        except:
          # if just needs user--> send to keyboard and click enter if possible
            count -= 1
            password_box = None

    return (password_box, count)

toplist = open("./top-1m.csv", "r")

for i in range(84):
    l = toplist.readline()

for siteCount in range(1, 1000):
    try:

        login_not_found = False

        l = toplist.readline()
        base = l.split(",")[1].strip()    
        if (l.split(",")[0] != "*"):
            url = "http://www." + base
        else:
            url = base

        records[base] = dict()

        # get website
        try:
            driver.get(url)
            records[base]['resolved'] = True
        except:
            urls_cannot_resolve.append(url)
            records[base]['resolved'] = False
            continue

        sleep(2) 

        # find sign in
        count = 27 # set this to the number of ways we are looking for the log in button
        while (count >= 0):
            try:
                if (count == 27): 
                    driver.find_element(By.XPATH, "//input[@id= 'loginUsername']").click() 
                    break
                if (count == 26): 
                    driver.find_element(By.XPATH, "//*[text()=' Sign In']").click() 
                    break
                if (count == 25): 
                    driver.find_element(By.XPATH, "//*[text()=' Sign In ']").click() 
                    break
                if (count == 24): 
                    driver.find_element(By.XPATH, "//*[text()='log in']").click() 
                    break
                if (count == 23): 
                    driver.find_element(By.XPATH, "//*[text()='login']").click()
                    break
                if (count == 22): 
                    driver.find_element(By.XPATH, "//*[text()='log-in']").click()
                    break
                if (count == 21): 
                    driver.find_element(By.XPATH, "//*[text()='log on']").click()
                    break
                if (count == 20): 
                    driver.find_element(By.XPATH, "//*[text()='Log on']").click(); 
                    break
                if (count == 19): 
                    driver.find_element(By.XPATH, "//*[text()='Log in']").click()
                    break
                if (count == 18): 
                    driver.find_element(By.XPATH, "//*[text()='Log-in']").click()
                    break
                if (count == 17): 
                    driver.find_element(By.XPATH, "//*[text()='Log In']").click(); 
                    break
                if (count == 16): 
                    driver.find_element(By.XPATH, "//*[text()='LOG-IN']").click()
                    break
                if (count == 15): 
                    driver.find_element(By.XPATH, "//*[text()='LOG IN']").click()
                    break
                if (count == 14): 
                    driver.find_element(By.XPATH, "//*[text()='LOGIN']").click()
                    break
                if (count == 13): 
                    driver.find_element(By.XPATH, "//*[text()='Hello, Sign in']").click() #thanks Amazon
                    break
                if (count == 12): 
                    driver.find_element(By.XPATH, "//*[text()='SignIn']").click()
                    break
                if (count == 11): 
                    driver.find_element(By.XPATH, "//*[text()='signIn']").click()
                    break
                if (count == 10): 
                    driver.find_element(By.XPATH, "//*[text()='signin']").click()
                    break
                if (count == 9): 
                    driver.find_element(By.XPATH, "//*[text()='sign-in']").click()
                    break
                if (count == 8): 
                    driver.find_element(By.XPATH, "//*[text()='sign in']").click()
                    break
                if (count == 7): 
                    driver.find_element(By.XPATH, "//*[text()='Sign-in']").click()
                    break
                if (count == 6): 
                    driver.find_element(By.XPATH, "//*[text()='Sign-In']").click()
                    break
                if (count == 5): 
                    driver.find_element(By.XPATH, "//*[text()='Sign in']").click(); 
                    break
                if (count == 4): 
                    driver.find_element(By.XPATH, "//*[text()='Sign In']").click()
                    break
                if (count == 3): 
                    driver.find_element(By.XPATH, "//*[text()='SIGN-IN']").click()
                    break
                if (count == 2): 
                    driver.find_element(By.XPATH, "//*[text()='SIGN IN']").click()
                    break
                if (count == 1): 
                    driver.find_element(By.XPATH, "//*[text()='SIGNIN']").click()
                    break
                if (count == 0):
                    login_not_found = True
                    urls_no_login.append(url) # no log in found
                    break 
                    
            except Exception as e:
                count -= 1
                continue
        
        if (not login_not_found):
            records[base]['login'] = count

        if (login_not_found):
            count = 4
            while (count >= 0):
                try:
                    if (count == 4): print()
                    elif (count == 3): driver.get(url + "/login")
                    elif (count == 2): driver.get(url + "/signin")
                    elif (count == 1): driver.get(url + "/sign_in")
                    elif (count == 0): records[base]['login'] = 0; break
                    if (find_username()[0]):
                        login_not_found = False
                        records[base]['login'] = count
                        break
                    else:
                        count -= 1
                except:
                    count -= 1

        if (login_not_found):
            continue

        # At this point, bot should be at login page... now look for username box
        sleep(2)

        (username_box, username_code) = find_username()
        (password_box, password_code) = find_password()

        records[base]['username'] = username_code
        records[base]['password'] = password_code

        if (username_box and password_box):
            username_box.send_keys(USERNAME)
            password_box.send_keys(PASSWORD)
            sleep(0.5)
            password_box.send_keys(Keys.ENTER)

        elif (username_box):
            username_box.send_keys(USERNAME)
            sleep(0.5)
            username_box.send_keys(Keys.ENTER)

        sleep(2)

        if (not password_box and username_box):
            (password_box, password_code) = find_password()
            records[base]['password'] = password_code
            if (password_box):
                password_box.send_keys(PASSWORD)
                sleep(0.5)
                password_box.send_keys(Keys.ENTER)
        
        sleep(2)

        try:
            x = driver.find_element(By.XPATH, "//iframe[@id='recaptcha-iframe']")
            driver.switch_to.frame(x)
            x = driver.find_element(By.XPATH, "//iframe[@title='reCAPTCHA']")
            driver.switch_to.frame(x)
        except:
            print("No recaptcha frame")

        count = 5 # set this to the number of ways we are looking for CAPTCHA
        while (count >= 0):
            try:
                if (count == 5): 
                    driver.find_element(By.XPATH, "//div[@role='checkbox']").click()
                    break
                if (count == 4): 
                    x = driver.find_element(By.XPATH, "//div[@class='recaptcha-checkbox-borderAnimation']")
                    x.click()
                    break
                if (count == 3): 
                    driver.find_element(By.XPATH, "//div[@role='checkbox']").click()
                    break
                if (count == 2): 
                    driver.find_element(By.XPATH, "//div[@id='recaptcha-accessible-status']").click()
                    break
                if (count == 1): 
                    driver.find_element(By.XPATH, "//span[@role='checkbox']").click()
                    break
                if (count == 0):
                    CAPTCHA_NOTFOUND = True
                    print(CAPTCHA_NOTFOUND)
                    break
            except:
                count -= 1
                continue

        # grab source code, dump to url
        source_code = driver.page_source
        with open("./sourcecode/"+ url.split(".")[1] + "_source.html", "w", encoding="utf-8") as f:
            f.write(source_code)
        # grab screen shot, save it
        driver.get_screenshot_as_file("./screenshots/" + url.split(".")[1] + "_screenshot.png")
    
    except Exception as E:
        print("Error found")
        print(E.with_traceback())


sleep(2)
print(records)
driver.close()



# TODO:
# DONE - Debug why facebook will not work
# DONE - Make sure the top 50 are able to grab the login page and input username password
# - Create signals for missed websites at different stages
# - Create retry functionality
# 
# TODO:
# - Create analysis script to parse source code
# - Read through top 25 to find captcha types
# - Try and trigger 10 websites manually
# 