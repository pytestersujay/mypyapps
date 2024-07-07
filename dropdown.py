import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()
country_element=Select(driver.find_element(By.XPATH,"//select[@id='input-country']"))
#country_element=Select(country_element)
"""country_element.select_by_visible_text("India")
country_element.select_by_value()
country_element.select_by_index()

#capture all the options and print them
all_options=country_element.options
print("total number of options:",len(all_options))
for opt in all_options:
    print(opt.text)

#select option from dropdown without using built-in method
for opt in all_options:
    if opt.text=="India":
        opt.click()
        break"""

"""assignement
Handle dropdowns avaialble in this site:
 https://itera-qa.azurewebsites.net/home/automation"""


