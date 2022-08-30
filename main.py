from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

driver.get("https://google.com")

search_bar = driver.find_element(By.NAME,"q")
search_bar.send_keys("cats",Keys.RETURN)

images = driver.find_element(By.LINK_TEXT, "Images")
images.click()
time.sleep(2)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(2)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(2)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

time.sleep(3)
driver.back()
driver.back()

search_bar = driver.find_element(By.NAME,"q")
search_bar.send_keys("bunnies",Keys.RETURN)

images = driver.find_element(By.LINK_TEXT, "Images")
images.click()

time.sleep(2)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(2)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(2)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")


time.sleep(5)
driver.quit()
