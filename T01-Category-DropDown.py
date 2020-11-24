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

# Selenium link click on the "Category" link using WebDriverWait Python
wait_variable.until(E.element_to_be_clickable((By.LINK_TEXT, "Category"))).click()
# Go back to the home page.
time.sleep(1)
# Click the same link but with the partial link text to Selenium link click
wait_variable.until(E.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "ANAK-ANAK"))).click()
time.sleep(3)
wait_variable.until(E.element_to_be_clickable((By.LINK_TEXT, "Category"))).click()
time.sleep(1)
wait_variable.until(E.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "CELANA"))).click()
time.sleep(3)
wait_variable.until(E.element_to_be_clickable((By.LINK_TEXT, "Category"))).click()
time.sleep(1)
wait_variable.until(E.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "DEWASA"))).click()
time.sleep(3)
wait_variable.until(E.element_to_be_clickable((By.LINK_TEXT, "Category"))).click()
time.sleep(1)
wait_variable.until(E.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "HELM"))).click()
time.sleep(3)
wait_variable.until(E.element_to_be_clickable((By.LINK_TEXT, "Category"))).click()
time.sleep(1)
wait_variable.until(E.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "JERSEY"))).click()
time.sleep(3)
wait_variable.until(E.element_to_be_clickable((By.LINK_TEXT, "Category"))).click()
time.sleep(1)
wait_variable.until(E.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "KACAMATA"))).click()
time.sleep(3)
wait_variable.until(E.element_to_be_clickable((By.LINK_TEXT, "Category"))).click()
time.sleep(1)
wait_variable.until(E.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "MOTORCROS"))).click()
time.sleep(3)
wait_variable.until(E.element_to_be_clickable((By.LINK_TEXT, "Category"))).click()
time.sleep(1)
wait_variable.until(E.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "SARUNG TANGAN"))).click()
time.sleep(3)
wait_variable.until(E.element_to_be_clickable((By.LINK_TEXT, "Category"))).click()
time.sleep(1)
wait_variable.until(E.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "SEPATU"))).click()
time.sleep(3)
wait_variable.until(E.element_to_be_clickable((By.LINK_TEXT, "Home"))).click()
time.sleep(3)
driver.quit()