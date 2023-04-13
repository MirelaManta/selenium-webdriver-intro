from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# steps to create the driver and keep the page open(with options)
chrome_driver_path = "C:\Development\chromedriver.exe"
service = Service(chrome_driver_path)
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=chr_options)

# opening web pages and finding specific elements
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# # article_count.click()
#
# help_desk = driver.find_element(By.LINK_TEXT, "Help desk")
# # help_desk.click()
#
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)


# -----------------------Challenge---------------------------
# Signup to The LAB Report
driver.get("https://londonappbrewery.com/sendy/subscription?f=m7Xj2bDOCQnlJ27yezLEAtJi1mhUIxOaJcJGZYMLLX6wx5MZd0b2FunBI8dOomNt&_ga=2.236530305.1069785959.1681129372-857321581.1681129372")
name = driver.find_element(By.NAME, "name")
name.send_keys("Mirela")
email = driver.find_element(By.NAME, "email")
email.send_keys("mirela.manta23@gmail.com")
driver.find_element(By.NAME, "gdpr").click()
recaptcha = driver.find_element(By.CLASS_NAME, "g-recaptcha")
recaptcha.click()
time.sleep(8)
driver.find_element(By.ID, "submit").click()
