import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



browser_name="chrome"
if(browser_name=="chrome"):
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.maximize_window();
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    #options = webdriver.ChromeOptions()
    #options.add_experimental_option("detach", True)

elif (browser_name=="firefox"):
    browser = webdriver.Firefox()
elif(browser_name == "edge"):
    browser = webdriver.edge()
browser.get('https://www.amazon.in/')


# browser.find_element(By.XPATH,"//i[@class='hm-icon nav-sprite']").click()
#
# best_sellers = browser.find_element(By.LINK_TEXT,'Best Sellers')
# browser.execute_script("arguments[0].click();",best_sellers)
# title= browser.execute_script('return document.title;')
# print(title)
# browser.execute_script("alert('hello');")

#inner_text= browser.execute_script("return document.documentElement.innerText;")
print(browser.execute_script('return document.documentElement.innerText'))
#print(inner_text)
browser.find_element(By.XPATH,"//i[@class='hm-icon nav-sprite']").click()
best_sellers = browser.find_element(By.LINK_TEXT,'Best Sellers')
browser.execute_script("arguments[0].click();",best_sellers)
title= browser.execute_script('return document.title;')
# print(title)
#browser.execute_script("alert('hello');")
#browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
time.sleep(1)

#element= WebDriverWait(browser,10).\
#    until(EC.presence_of_element_located(By.XPATH,"//h2[normalize-space()='Bestsellers in Office Products']"))

element= browser.find_element(By.XPATH,"//h2[normalize-space()='Bestsellers in Office Products']")

browser.execute_script("arguments[0].scrollIntoView(true);", element)

print(browser.execute_script("return navigator.userAgent;"))  # how to get user agent


time.sleep(5)
