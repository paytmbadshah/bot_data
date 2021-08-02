import telebot
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import os
from random import randint

Bot_Token = "1898423485:AAFlOjODoAOwTVlOygTaafa6D1Jt_y8TMqo"

bot = telebot.TeleBot(Bot_Token, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN


user_dict = {}


from selenium import webdriver
import time 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from random import randint



my_username = "" # Instagram Username 
my_password = "saharsh_2" # Instagram Password 



to_search = "pubg"

def insta_login():
    browser = webdriver.Chrome(executable_path=r"C:\Chrome_driver\chromedriver.exe")  # Creating Object Of Chrome  && executable_path=r"C:\path\to\chromedriver.exe"
    browser.get("https://www.instagram.com/")
    browser.maximize_window()
    time.sleep(10)
    browser.save_screenshot("logo.jpg")
    # username_input = browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(my_username)
    # password_input = browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(my_password)
    # time.sleep(3)
    # login_button_input = browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[3]/button").click()
    # time.sleep(5)
    # not_now_button = browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button").click()
    # time.sleep(5)
    # off_notifi_button = browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
    # time.sleep(5)
    return True





@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    chat_id = message.chat.id
    text_to_send= "Wel-Come To The Bot  "
    text = bot.send_message(message.chat.id , text_to_send)
    time.sleep(5)
    # bot.send_photo(chat_id, photo=open('logo.jpg', 'rb'))
    login = insta_login()
    time.sleep(15)
    bot.send_photo(chat_id, photo=open('logo.jpg', 'rb'))
    time.sleep(10)
    browser.close()
    # if login == True:
    #     for i in range(5):
    #         try:
    #             browser.get("https://www.instagram.com/"+to_search)
    #             time.sleep(10)
    #             click_follower_button = browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click()
    #             time.sleep(10)
    #             follow_profile_button = browser.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/ul/div/li[1]/div/div[3]/button").click()
    #             time.sleep(10)
    #             browser.refresh()
    #             time.sleep(randint(25,60))
    #         except:
    #             pass    
    # else:
    #     print("Login Error !!")





        
while True:
    try:
        bot.polling()
    except:
        time.sleep(10)