import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
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
browser.implicitly_wait(30)

browser.find_element(By.LINK_TEXT,"Amazon miniTV").click()

time.sleep(2)

browser.back()
time.sleep(2)
browser.forward()
time.sleep(2)
