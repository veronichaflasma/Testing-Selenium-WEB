# Selenium WebDriver Python coding
# Import webdriver library to use the Selenium WebDriver commands.
from idlelib import browser

from selenium import webdriver
# Import the By library to find the links on the web page.
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E
import time

exec_path = r"D:\APPLICATION\Driver\geckodriver.exe"
URL = r"http://localhost/OnlineShop/"
wait_time_out = 15

driver = webdriver.Firefox(executable_path=exec_path)
# Navigate to the URL.
driver.get(URL)
wait_variable = W(driver, wait_time_out)

# We need to find the link before Python Selenium click link .
# Define the Python list called links.
links = wait_variable.until(E.visibility_of_any_elements_located((By.TAG_NAME, "a")))
print ("The total number of links is", len(links))
# Use for each loop to python selenium loop through links. It takes time to loop through links.
for link in links:
    print (link.text) # Selenium link text

# Selenium link click on the "NavigationBar" link using WebDriverWait Python
wait_variable.until(E.element_to_be_clickable((By.LINK_TEXT, "Tentang Kami"))).click()
time.sleep(3)
wait_variable.until(E.element_to_be_clickable((By.LINK_TEXT, "Cara Belanja"))).click()
time.sleep(3)
wait_variable.until(E.element_to_be_clickable((By.LINK_TEXT, "Hubungi Kami"))).click()
time.sleep(3)
wait_variable.until(E.element_to_be_clickable((By.LINK_TEXT, "Keranjang Belanja"))).click()
time.sleep(3)
wait_variable.until(E.element_to_be_clickable((By.LINK_TEXT, "Home"))).click()
time.sleep(3)
driver.quit()