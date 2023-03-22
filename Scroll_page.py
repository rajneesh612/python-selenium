from selenium import webdriver

# import Action chains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# create webdriver object
driver = webdriver.Firefox()
driver.maximize_window()
# get method to launch the URL
driver.get ("https://www.softwaretestingmaterial.com/")
# to scroll with Javascript executor
driver.execute_script ("window.scrollTo(0,document.body.scrollHeight);")