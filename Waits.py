import time

from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

browser_name="chrome"
if(browser_name=="chrome"):
    options= Options()
    options.add_argument('--headless')

    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)
    browser.maximize_window();
    chrome_options = Options()

    chrome_options.add_experimental_option("detach", True)
    #options = webdriver.ChromeOptions()
    #options.add_experimental_option("detach", True)

elif (browser_name=="firefox"):
    browser = webdriver.Firefox()
elif(browser_name == "edge"):
    browser = webdriver.edge()


browser.get('https://www.rediff.com/')
