from curses import KEY_A1
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import *
from time import sleep
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

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
# urls = ["https://www.google.com","https://www.yahoo.com", "https://www.amazon.com", "https://www.reddit.com", "https://www.instagram.com", "https://en.wikipedia.org/wiki/Main_Page", "https://www.bing.com", "https://www.linkedin.com", "https://www.twitter.com", "https://www.zoom.us", "https://www.ebay.com", "https://www.office.com", "https://www.live.com",  "https://www.fandom.com/", "https://www.microsoft.com", "https://www.nytimes.com"]
#restricted sites= ["https://www.chaturbate.com","https://www.xvideos.com"]
#websitesnotfound= ["https://microsoftonline.com"]
#  "https://www.facebook.com"

urls = ["https://www.reddit.com/login"]

urls_found_signin_btn = 0
urls_no_login = []

def find_password():
    
    # password find
    # ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/autocomplete and https://www.lambdatest.com/blog/locators-in-selenium-webdriver-with-examples/
    count = 8 # set this to the number of ways we are looking for the log in button
    password_box = None
    while (count >= 0):
        try:
            if (count == 9):
                password_box = driver.find_element(By.XPATH, "//input[@id= 'loginPassword']")
                password_box.send_keys("P")
                break
            if (count == 8):
                password_box = driver.find_element(By.XPATH, "//select[@autocomplete= 'new-password']")
                password_box.send_keys("P")
                break
            if (count == 7):
                password_box = driver.find_element(By.XPATH, "//input[@autocomplete= 'new-password']")
                password_box.send_keys("P")
                break
            if (count == 6):
                password_box = driver.find_element(By.XPATH, "//textarea[@autocomplete= 'new-password']")
                password_box.send_keys("P")
                break
            if (count == 5):
                password_box = driver.find_element(By.XPATH, "//select[@autocomplete= 'current-password']")
                password_box.send_keys("P")
                break
            if (count == 4):
                password_box = driver.find_element(By.XPATH, "//input[@autocomplete= 'current-password']")
                password_box.send_keys("P")
                break
            if (count == 3):
                password_box = driver.find_element(By.XPATH, "//textarea[@autocomplete= 'current-password']")
                password_box.send_keys("P")
                break
            if (count == 2):
                password_box = driver.find_element(By.XPATH, "//input[@id= 'password']")
                password_box.send_keys("P")
                break
            if (count == 1):
                password_box = driver.find_element(By.XPATH, "//input[@name= 'password']")
                password_box.send_keys("P")
                break
            if (count == 0):
                print(url + ": no password box found in login page")
                break
        except:
          # if just needs user--> send to keyboard and click enter if possible
            count -= 1
            password_box = None

    return password_box

for url in urls:

    # get website
    driver.get(url)
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

    # At this point, bot should be at login page... now look for username box
    sleep(1)
    urls_found_signin_btn += 1 # increment counter of urls_found_signin

    # username find
    # ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/autocomplete and https://www.lambdatest.com/blog/locators-in-selenium-webdriver-with-examples/
    count = 11 # set this to the number of ways we are looking for the log in button
    username_box = None
    while (count >= 0):
        try:
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

    password_box = find_password()

    if (username_box and password_box):
        username_box.send_keys("ece8803@hotmail.com")
        password_box.send_keys("Password1!" + Keys.ENTER)
    elif (username_box):
        username_box.send_keys("ece8803@hotmail.com" + Keys.ENTER)

    sleep(2)

    password_box = find_password()

    if (password_box):
        password_box.send_keys("Password1!" + Keys.ENTER)

    sleep(2)

    # grab source code, dump to url
    source_code = driver.page_source
    with open("./sourcecode/"+ url.split(".")[1] + "_source.html", "w", encoding="utf-8") as f:
        f.write(source_code)
    # grab screen shot1, save it
    driver.get_screenshot_as_file("./screenshots/" + url.split(".")[1] + "_screenshot.png")

    #foucsed something 


print(urls_no_login) # prints out webpages without a login button- may include those already on a login page- IG, linkeDIn
sleep(2)
driver.close()





### WORK BOX BELOW - IGNORE ###

#'''


    # find username password input boxes
    # driver.find_element(By.ID, "login-username").send_keys("hotdog@hotdog.com" + Keys.ENTER)
    # 
    
    #x.send_keys("hotdog@hotdog.com")
    #x = driver.find_element(By.ID, "pass")
    #x.send_keys("SUHSUHSUH1!" + Keys.ENTER)
    #sleep(2) 

    # grab source code, dump to url
    #source_code = driver.page_source
    #with open(url[12:-4] + "_source.html", "w", encoding="utf-8") as f:
        #f.write(source_code)

    # grab screen shot, save it
    # driver.get_screenshot_as_file(url[12:-4] + "_screenshot.png")

    #print(source_code.find("recaptcha"))

    #driver.send_keys("")

    #driver.close()

'''
        if (count == 10): x = driver.find_element(By.__text_signature__, "user")
        if (count == 9): x = driver.find_element(By.__text_signature__, "login-username")
        if (count == 8): x = driver.find_element(By.__text_signature__, "username")
        if (count == 7): x = driver.find_element(By.__text_signature__, "email")
        if (count == 6): x = driver.find_element(By.__text_signature__, "Email")
        if (count == 5): x = driver.find_element(By.__text_signature__, "Email or Phone")
        if (count == 4): x = driver.find_element(By.__text_signature__, "Email or phone")
        if (count == 3): x = driver.find_element(By.__text_signature__, "email or phone")
        if (count == 2): x = driver.find_element(By.__text_signature__, "Phone")
        if (count == 1): x = driver.find_element(By.__text_signature__, "phone")
'''




#1. have a list of URLs want to access alexa top 50

#2. search the page for a sign in link, click on it
 #-> try different casing/phrasing of this

#3. search the page for username and password slots, put in info, hit enter/ find submit
 #-> autocomplete tag? 

#4. grab the source code after the attempt, take a screenshot and save it, take the source code and save it,

#...

 #1. search for recaptcha string and update some dictionary to keep track as you traverse through source code

#'''