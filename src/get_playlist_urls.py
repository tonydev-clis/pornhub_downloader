from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time
driver = webdriver.Chrome()
playlist_url = input("Enter playlist url: ")
driver.get(playlist_url)

SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
links = [x.get_attribute("href") for x in driver.find_elements(By.CSS_SELECTOR, "div > div.thumbnail-info-wrapper.clearfix > span > a")]

with open('./data/data.json', 'w') as file:
    json.dump({"downloaded_links": links}, file, indent=4)

