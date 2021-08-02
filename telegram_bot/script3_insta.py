import telebot
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import os
from random import randint

Bot_Token = "1818731775:AAHI5YdDqpBcKUhE1iGNwRXTOvCUAyvhwT8"

bot = telebot.TeleBot(Bot_Token, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN


user_dict = {}


class User:
    def __init__(self, username):
        self.username = username
        self.password = None
        self.count = None
        self.to_search = None


@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    text_to_send= "Welcome To The Auto Follow Bot \n \n Enter Your Instagram Username : "
    bot.register_next_step_handler(bot.send_message(message.chat.id , text_to_send), process_username_step)


def process_username_step(message):
    try:
        chat_id = message.chat.id
        username = message.text
        user = User(username)
        user_dict[chat_id] = user
        msg = bot.reply_to(message, 'Got It !! \n \n Now Enter Your Password : ')
        bot.register_next_step_handler(msg, process_password_step)
    except Exception as e:
        bot.reply_to(message, 'oooops Try Again !!')


def process_password_step(message):
    try:
        chat_id = message.chat.id
        password = message.text
        user = user_dict[chat_id]
        user.password = password
        msg = bot.reply_to(message, 'Got It !! \n \n Now Enter The Instagram Page Thats FOllower You Want To Follow : ')
        bot.register_next_step_handler(msg, process_follow_account_step)
    except Exception as e:
        bot.reply_to(message, 'oooops Try Again !!')


def process_follow_account_step(message):
    try:
        chat_id = message.chat.id
        to_search = message.text
        user = user_dict[chat_id]
        user.to_search = to_search
        msg = bot.reply_to(message, 'Got It !! \n \n Now Enter Count i.e. How Many Times You Wan To Run It : ')
        bot.register_next_step_handler(msg, process_count_step)
    except Exception as e:
        bot.reply_to(message, 'oooops Try Again !!')


def process_count_step(message):
    try:
        chat_id = message.chat.id
        count = message.text
        user = user_dict[chat_id]
        user.count = count
        ms=bot.send_message(chat_id, "Got Everthing Confirm it \n \n Username : " + user.username + "\n Password:" + user.password +" \n \n Follow This Accounts Follower : "+user.to_search+"\n Count : "+str(user.count)+"\n \n Type 'YES' To Continue Or 'NO' Exit")
        bot.register_next_step_handler(ms, process_insta_step)
    except Exception as e:
        bot.reply_to(message,'oooops')

def process_insta_step(message):
    chat_id = message.chat.id
    check = message.text
    if check == "YES":
        user = user_dict[chat_id]
        msgs=bot.send_message(chat_id, " Task : Loading Browser !!")
        try:
            # chrome_options = webdriver.ChromeOptions()
            # chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
            # chrome_options.add_argument("--headless")
            # chrome_options.add_argument("--disable-dev-shm-usage")
            # chrome_options.add_argument("--no-sandbox")
            # browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
            browser = webdriver.Chrome(executable_path=r"C:\Chrome_driver\chromedriver.exe")
        except:
            bot.send_message(chat_id,"Task Failed : I Got An error While Loading Browerser")
            # browser.close()
            exit()

        # try:
        bot.edit_message_text(chat_id=chat_id, text="Task : Browser Loaded Trying To Login", message_id=msgs.message_id)
        browser.get("https://www.instagram.com/")
        time.sleep(20)
        logins_button_input = browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/article/div/div/div/div[3]/button[1]").click()
        time.sleep(20)
        bot.edit_message_text(chat_id=chat_id, text="Login Button Pe Click Kara ", message_id=msgs.message_id)
        username_input = browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(user.username)
        bot.edit_message_text(chat_id=chat_id, text="Entered Username", message_id=msgs.message_id)
        password_input = browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(user.password)
        bot.edit_message_text(chat_id=chat_id, text="Entered Login Details", message_id=msgs.message_id)
        time.sleep(3)
        login_button_input = browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[3]/button").click()
        bot.edit_message_text(chat_id=chat_id, text="Clicked On Login Button", message_id=msgs.message_id)
        time.sleep(13)
        not_now_button = browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button").click()
        time.sleep(13)
        off_notifi_button = browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
        time.sleep(10)
        bot.edit_message_text(chat_id=chat_id, text="Login Successfully \n \n Task Following User", message_id=msgs.message_id)
        
        # except:
        #     bot.edit_message_text(chat_id=chat_id, text="TaskIncorrect Details Entered", message_id=msgs.message_id)
        #     browser.close()
        #     exit()
        
        # browser = webdriver.Chrome(executable_path=r"C:\Chrome_driver\chromedriver.exe")  # Creating Object Of Chrome  && executable_path=r"C:\path\to\chromedriver.exe"
        time.sleep(10)
        for i in range(int(user.count)):
            try:
                browser.get("https://www.instagram.com/"+user.to_search)
                time.sleep(10)
                click_follower_button = browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click()
                time.sleep(10)
                follow_profile_button = browser.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/ul/div/li[1]/div/div[3]/button").click()
                time.sleep(10)
                bot.edit_message_text(chat_id=chat_id, text="Follow "+str(i)+"User \n \n Waiting For Some Time To Bypass Blocking ", message_id=msgs.message_id)
                browser.refresh()
                time.sleep(randint(40,100))
            except:
                pass
        browser.close()
        bot.edit_message_text(chat_id=chat_id, text="Task Completed : Followed "+str(user.count)+"User", message_id=msgs.message_id)
    else:
        bot.send_message(chat_id,"Canceled The Proccess")
        exit()
        

bot.polling()
