from selenium import webdriver

PATH = "C:/Users/hussa/Documents/chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://www.yahoo.com")
print(driver.title)
driver.close()