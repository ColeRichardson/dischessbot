import requests
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")

url = "https://lichess.org/"

webdriver = # path to webdriver
#"C:/Users/ColeR/Documents/chromedriver.exe"
driver = Chrome(options=chrome_options, executable_path=webdriver)
driver.get(url)
button = driver.find_element_by_id('SummonerRefreshButton')
button.click()