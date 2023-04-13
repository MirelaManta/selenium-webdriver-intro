from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# selenium package contains code for us to be able to interact with browsers
# a web driver is like a bridge that tells selenium how to interact with a specific browser

chrome_driver_path = "C:\Development\chromedriver.exe"
service = Service(chrome_driver_path)
# these option is needed to keep the browser open after launching
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=chr_options)
#-------------------------------------------------------------------------------------------------
# driver.get("https://www.amazon.com/COSORI-Airfryer-Dishwasher-Safe-freidora-Exclusive/dp/B0936FGLQS/ref=sr_1_2_sspa?crid=3QU2DDJ38E353&keywords=air%2Bfryer&qid=1680959373&sprefix=air%2Bfrayer%2Caps%2C430&sr=8-2-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzT00xVjBURUo1VkRKJmVuY3J5cHRlZElkPUEwNjc1NzA4MlFENEdYQkFaWjY1NSZlbmNyeXB0ZWRBZElkPUEwMzc0MTkwVzRCT0lFUUZIQzhQJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ&th=1")
#
# # Task from previous lesson, Automated Price Tracker
# # I couldn't use the class for the whole price, so I did this...does the job
# # price = driver.find_element(By.CLASS_NAME, "a-offscreen")
# # print(price.text)
# currency = driver.find_element(By.CLASS_NAME, "a-price-symbol")
# price_whole = driver.find_element(By.CLASS_NAME, "a-price-whole")
# price_fraction = driver.find_element(By.CLASS_NAME, "a-price-fraction")
# price = f"{currency.text}{price_whole.text}.{price_fraction.text}"
# print(price)

# --------------------------------------------------------------------------------------------
driver.get("https://python.org/")
# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.get_attribute("placeholder"))
# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)

# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# in a class doc-widget, find an anchor tag ^^
# print(documentation_link.text)

# submit_bug_link = driver.find_element(By.XPATH, "//*[@id='site-map']/div[2]/div/ul/li[3]/a")
# print(submit_bug_link.text)

# ------------------------Challenge---------------------------------------------------------
dates_wd_elements = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_dates = [date.text for date in dates_wd_elements]

events_wd_elements = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
event_names = [event.text for event in events_wd_elements]
events = {}

for n in range(len(event_dates)):
    events[n] = {
        "time": event_dates[n],
        "name": event_names[n]
    }
print(events)


# driver.close()  # closes a single tab, where has been opened a particular page
driver.quit()  # quits the entire browser
