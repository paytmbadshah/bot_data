import Credential

from instabot import Bot

import os

if os.path.isfile(Credential.path+"config/thebattlegroundmobileindia_uuid_and_cookie.json"):
    os.remove(Credential.path+"config/thebattlegroundmobileindia_uuid_and_cookie.json")


bot = Bot()

# Login The Bot 
bot.login(username=Credential.my_username, password=Credential.my_password,force=True)

print("\n \n ------------------------------------------------------------------------------------------------------")

#Asking User To Input Username Of The Instagram User To Get His Followers 
insta_username = input("\n \n Enter Instagram Username : ")

# Getting Follower Using Isnta Bot 
followers=bot.get_user_followers(insta_username)

#  Writing The Follower To The List
with open(Credential.path+"follower_list.txt","w") as f:
	for follower in followers:
		f.write(follower+"\n")
f.close()

# Successfull Message
print("\n \n  \t \t Followers Fetched Succssfully : File Name : follower_list.txt")
print("\n \n ------------------------------------------------------------------------------------------------------")

# user_id = bot.get_user_id_from_username(username)

# for follower in followers:
#      print(follower)

# medias=bot.get_user_medias(user_id) #followers[0]

# for media in medias:
#      bot.like(media)