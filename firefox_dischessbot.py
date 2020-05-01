#import requests
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

#chrome_options = Options()
#chrome_options.add_argument("--headless")

url = "https://lichess.org/setup/friend"

browser = "/usr/bin/geckodriver"
#"C:/Users/ColeR/Documents/chromedriver.exe"
driver = webdriver.Firefox()
driver.get(url)
time.sleep(5)
button = driver.find_element_by_css_selector('button.random')
button.click()
play_link = driver.find_element_by_id('challenge-id')
play_link = play_link.get_attribute('value')
print(play_link)
