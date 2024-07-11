import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.select import Select
#http://the-internet.herokuapp.com/basic_auth
#http://username:password@test. com the-internet.herokuapp.com/basic_auth
driver=webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/basic_auth")
driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.maximize_window()
time.sleep(5)
