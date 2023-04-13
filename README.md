# Selenium WebDriver Introduction

This repository contains sample code to demonstrate the use of the Selenium WebDriver to interact with a web browser. It includes an example script to:
* Launch the Chrome browser using a WebDriver
* Load different web pages
* Extract data from those pages using Selenium's By module to locate elements
* Output the extracted data to the console

## Installation

To use this code, you will need to install:
* Python (version 3 or above)
* The Selenium package for Python (__pip install selenium__)

You will also need to download the appropriate WebDriver executable for your version of Chrome and operating system.
## Usage
1. Clone or download this repository to your local machine.
2. Modify the __chrome_driver_path__ variable in main.py to point to the location of the downloaded WebDriver executable on your machine.
3. Open a terminal or command prompt and navigate to the directory containing main.py.
4. Run the command python main.py to execute the script.

## Notes
* The script uses Selenium's webdriver.Chrome class to launch the Chrome browser and connect to the ChromeDriver executable. It also uses Selenium's Options class to specify an option to keep the browser window open after the script has finished executing.
* Examples of extracted data from the Python.org home page:
  * The text in the search bar placeholder
  * The dimensions of the Python logo image
  * The text of the "Submit a Bug" link in the site map
  * The text and date of upcoming events listed in the "event-widget" class
 * The code in __interaction.py__ includes commented out code for navigating to the Wikipedia homepage and performing a search and an example on how to automate signing up for a newsletter on a website.
  * The script is currently set up to handle a reCAPTCHA. The time.sleep(8) line provides a pause for the user to complete the reCAPTCHA before the script proceeds to click the submit button. This may need to be adjusted depending on the website and how long the reCAPTCHA takes to complete.       
