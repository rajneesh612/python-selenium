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

browser.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
browser.implicitly_wait(30)

username = browser.find_element(By.XPATH,"//input[@placeholder='Username']")
username.send_keys("Admin")
password = browser.find_element(By.XPATH,"//input[@placeholder='Password']")
password.send_keys("admin123")
login_btn = browser.find_element(By.XPATH,"//button[normalize-space()='Login']")
login_btn.click()
time.sleep(10)
#assert 'Google' in browser.title