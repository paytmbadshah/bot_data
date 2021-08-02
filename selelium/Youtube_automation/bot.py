import os
from selenium import webdriver
import time 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from random import randint, random
import requests

url = "https://freekamall.tech/sms-bomber/1.php?sent=2&&count=100&&mobno=9399509374"

video_lists = ['https://youtu.be/A9L4ouBHSSo','https://youtu.be/AOL_jYPFRO8','https://youtu.be/s8Ul0-pQyso']
# for i in range(0,10):
#     x=randint(0,len(video_lists)-1)
#     video=video_lists[x]

# # req = requests.get(url)    
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--incognito")
chrome_options.add_argument("--kiosk")
browser = webdriver.Chrome(executable_path=r"C:\Chrome_driver\chromedriver.exe", options=chrome_options)       
browser.get('https://youtu.be/AOL_jYPFRO8')
play_button = browser.find_element_by_id('movie_player').click()


# for i in range(0,3):
#     chrome_options = webdriver.ChromeOptions()
#     # chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
#     # chrome_options.add_argument("--headless")
#     # chrome_options.add_argument("--disable-dev-shm-usage")
#     # chrome_options.add_argument("--no-sandbox")
#     # chrome_options.add_argument("--incognito")
#     chrome_options.add_argument("--kiosk")
#     # browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
#     browser = webdriver.Chrome(executable_path=r"C:\Chrome_driver\chromedriver.exe")
#     for i in video_lists:
#         browser.get(i)
#         time.sleep(3)
#         # play_button = browser.find_element_by_xpath('//*[@id="movie_player"]/div[26]/div[2]/div[1]/button').click()
        
#         time.sleep(10)
#     browser.close()
#     time.sleep(5)

      