# Selenium WebDriver Python coding
from selenium import webdriver
from selenium.webdriver.common.by import By
# Import statements for explicit wait
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E
import time

exec_path = r"D:\APPLICATION\Driver\geckodriver.exe"
URL = r"http://localhost/OnlineShop/"
wait_time_out = 15
# Define a list of locators for the language links.
search_locator = "cari"
search_text = "Jersey"
wait_time = 5

driver = webdriver.Firefox(executable_path=exec_path)
# Navigate to the URL.
driver.get(URL)
# Define the wait variable for explicit wait.
wait = W(driver, wait_time)
driver.maximize_window()
input_box_element = wait.until(E.presence_of_element_located((By.NAME, search_locator)))
time.sleep(3)
input_box_element.send_keys(search_text)
time.sleep(5)
input_box_element.submit()
# Pause the script for a few seconds.
time.sleep(5)
driver.back()
# driver.quit()