
import Credential

from instabot import Bot

import os

import time 

from random import * 


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


if os.path.isfile(Credential.path+"config/"+Credential.my_username+"_uuid_and_cookie.json"):
    os.remove(Credential.path+"config/"+Credential.my_username+"_uuid_and_cookie.json")


bot = Bot(
    filter_users=False, 
    filter_private_users=False,
    follow_delay=10
    )


# Login The Bot 
bot.login(username=Credential.my_username, password=Credential.my_password,force=True)


bot.approve_pending_follow_requests()

print("Completed")