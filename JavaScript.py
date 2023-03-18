import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By



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


browser.find_element(By.XPATH,"//i[@class='hm-icon nav-sprite']").click()

best_sellers = browser.find_element(By.LINK_TEXT,'Best Sellers')
browser.execute_script("arguments[0].click();",best_sellers)
title= browser.execute_script('return document.title;')
print(title)
browser.execute_script("alert('hello');")

inner_text= browser.execute_script('return document.documentElement.innerText')
print(inner_text)
time.sleep(1)