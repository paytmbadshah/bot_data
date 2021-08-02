from selenium import webdriver
import time 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(executable_path=r"C:\Chrome_driver\chromedriver.exe")  # Creating Object Of Chrome  && executable_path=r"C:\path\to\chromedriver.exe"

mobile_number = "7223889629"
no_otp = 10

for i in range(0,3):
    browser.get("https://mytoolstown.com/smsbomber/")
    mobile_number_input = browser.find_element_by_css_selector("input[id='mobno']").send_keys(mobile_number)
    time.sleep(3)
    count_input = browser.find_element_by_css_selector("input[id='count']").send_keys(no_otp)
    count_input = browser.find_element(By.XPATH,"//*[@id='sendsms']/div[3]/div/div/div[3]/label").click()
    time.sleep(3)
    submit_button = browser.find_element_by_xpath("//*[@id='startsms']").click()
    time.sleep(20)
    browser.refresh()
    time.sleep(180)

browser.close()