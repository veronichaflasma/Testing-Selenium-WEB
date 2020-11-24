# Selenium WebDriver Python coding
# Import webdriver library to use the Selenium WebDriver commands.
from idlelib import browser

from selenium import webdriver
# Import the By library to find the links on the web page.
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
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
time.sleep(5)
wait_variable.until(E.element_to_be_clickable((By.LINK_TEXT, "Add to cart"))).click()
time.sleep(3)

#Dropdown qty
element = driver.find_element_by_name("qty[]")
drp = Select(element)
drp.select_by_visible_text('2')
time.sleep(3)

#click update keranjang
wait_variable.until(E.element_to_be_clickable((By.XPATH, "/html/body/section/div/form/div[1]/input"))).click()
time.sleep(5)

#click selesai belanja
wait_variable.until(E.element_to_be_clickable((By.XPATH, "/html/body/section/div/form/div[1]/a[2]/div"))).click()
time.sleep(5)

#Fill form
fill_form = wait_variable.until(E.presence_of_element_located((By.NAME, "penerima")))
fill_form.send_keys("Veronicha")
time.sleep(2)
fill_form = wait_variable.until(E.presence_of_element_located((By.NAME, "email")))
fill_form.send_keys("veronichaflasma@gmail.com")
time.sleep(2)
fill_form = wait_variable.until(E.presence_of_element_located((By.NAME, "alamat")))
fill_form.send_keys("Malang")
time.sleep(2)
fill_form = wait_variable.until(E.presence_of_element_located((By.NAME, "no_telepon")))
fill_form.send_keys("082338118330")
time.sleep(2)
fill_form = wait_variable.until(E.presence_of_element_located((By.NAME, "propinsi")))
fill_form.send_keys("Jawa Timur")
time.sleep(2)
fill_form = wait_variable.until(E.presence_of_element_located((By.NAME, "kota")))
fill_form.send_keys("Malang")
time.sleep(2)
fill_form = wait_variable.until(E.presence_of_element_located((By.NAME, "kode_pos")))
fill_form.send_keys("65125")
time.sleep(2)

#choose metode pembayaran BCA
metode_pay = driver.find_element_by_name("bank_id")
pay = Select(metode_pay)
pay.select_by_visible_text('BCA- 12342456')
time.sleep(3)

#choose jasa pengiriman JNE
jasa_pengiriman = driver.find_element_by_name("jasapengiriman_id")
jasa = Select(jasa_pengiriman)
jasa.select_by_visible_text('JNE')
time.sleep(3)

#submit form
fill_form.submit()
time.sleep(5)

