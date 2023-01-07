from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import pandas as pd

url = 'https://www.artsy.net/collect'
driver = webdriver.Chrome()
driver.get(url)
arts = driver.find_elements(By.CLASS_NAME, 'Box-sc-15se88d-0')
print(arts)
# name full xpath => /html/body/div[2]/div/div/main/div/div/div[2]/div/div[2]/div/div[5]/div/div/div[1]/div[1]/div[1]/a/div/div[1]/div
for art in arts:
    print(art.find_element(By.XPATH, './/*[@id="main"]'))
#     print(art_name)
    # print(video.find_element(By.XPATH, ))
    # title = video.find_element(By.XPATH, './/*[@id="video-title-link"]').parent
    # views = video.find_element(By.XPATH, './/*[@id="metadata-line"]/span[2]').text
    # print(title)
