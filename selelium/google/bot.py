from selenium import webdriver
import time 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from random import randint, random, shuffle
import undetected_chromedriver.v2 as uc


def gen_chanel_name():
    fname_list=['technical','tech','tulsi','gaming','beast','boost','lapai','crry','minati']
    lname_list=['ram','syam','tech','technical','tele','radhe','anivesh','parag','surag','sindhi','gundi','gannesh','papi','alsi','sunda']
    cname = fname_list[randint(0,len(fname_list))]+" " + lname_list[randint(0,len(lname_list))]
    return cname


yt_chanels=['https://www.youtube.com/channel/UC-KjUEoANQJ3OvH31EPD5Ag','https://www.youtube.com/channel/UCpJcgxp8LI_0VmQ3tc-0BIA']

# ram1921desai323@gmail.com

# chrome_options = webdriver.ChromeOptions()
#         # chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
#         # chrome_options.add_argument("--headless")
#         # chrome_options.add_argument("--disable-dev-shm-usage")
#         # chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--incognito")
# chrome_options.add_argument("--kiosk")
# browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)


# browser.get()


gmailId="paytmbadshah102@gmail.com"
passWord = "7223889629"


options = uc.ChromeOptions()
options.add_argument("--kiosk")
# just some options passing in to skip annoying popups
options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
driver = uc.Chrome(executable_path="C:\Chrome_driver\chromedriver.exe")
driver.delete_all_cookies()



def gmail_login():
    driver.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2Fusers%2Fstory%2Fcurrent%27')
    time.sleep(10)
    driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
    driver.find_element_by_id('identifierId').send_keys(gmailId)
    driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
    time.sleep(10)
    driver.find_element_by_xpath('//input[@type="password"]').send_keys(passWord)
    time.sleep(10)
    driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
    time.sleep(10)



def create_new_chanel():
    driver.get('https://youtube.com')
    time.sleep(10)
    driver.get('https://www.youtube.com/account')
    time.sleep(10)
    try:
        add_chanel=driver.find_element_by_link_text('Add or manage your channel(s)').click()
        time.sleep(10)
        add=driver.find_element_by_css_selector('#contents > ytd-button-renderer > a').click()
        time.sleep(10)
    except:
       try:
            add_chanel=driver.find_element_by_link_text('Create a new channel').click()
            time.sleep(15)
       except:
            pass

    time.sleep(30)
    random_chanel_name=gen_chanel_name()
    enter_chanel_name=driver.find_element_by_id('PlusPageName').send_keys(random_chanel_name)
    time.sleep(5)
    check_tnc=driver.find_element_by_css_selector('#ConsentCheckbox').click()
    time.sleep(10)
    subscribe_btn=driver.find_element_by_id('submitbutton').click()
    time.sleep(30)
    



def subscribe_chanel():
    for chanel in yt_chanels:
        driver.get(chanel)
        time.sleep(10)
        subscribe_btn=driver.find_element_by_id('subscribe-button').click()
        time.sleep(10)


login_the_account = gmail_login()

for i in range(0,10):
    try:
        create_youtube_chanel = create_new_chanel()
        time.sleep(5)
        subscribe_to_chanel = subscribe_chanel()
    except:
        pass

print("DONE")
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--incognito")
# # chrome_options.add_argument("--kiosk")
# chrome_options.add_argument("--lang=en-us")
# driver = webdriver.Chrome(executable_path=r"C:\Chrome_driver\chromedriver.exe", options=chrome_options)    
# driver.get(r'https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
# driver.implicitly_wait(15)
  
# loginBox = driver.find_element_by_xpath('//*[@id ="identifierId"]')
# loginBox.send_keys(gmailId)
  
# nextButton = driver.find_elements_by_xpath('//*[@id ="identifierNext"]')
# nextButton[0].click()
  
# passWordBox = driver.find_element_by_xpath(
#         '//*[@id ="password"]/div[1]/div / div[1]/input')
# passWordBox.send_keys(passWord)
  
# nextButton = driver.find_elements_by_xpath('//*[@id ="passwordNext"]')
# nextButton[0].click()
 
# print('Login Successful...!!')




# for i in range(0,3000):
#     try:    
#         # browser = webdriver.Chrome(executable_path=r"C:\Chrome_driver\chromedriver.exe",chrome_options=chrome_options)  # Creating Object Of Chrome  && executable_path=r"C:\path\to\chromedriver.exe"
#         chrome_options = webdriver.ChromeOptions()
#         chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
#         chrome_options.add_argument("--headless")
#         chrome_options.add_argument("--disable-dev-shm-usage")
#         chrome_options.add_argument("--no-sandbox")
#         chrome_options.add_argument("--incognito")
#         chrome_options.add_argument("--kiosk")
#         browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
#         for i in video_lists:
#             browser.get(i)
#             time.sleep(10)
#         browser.close()
#         time.sleep(5)
#     except:
#         pass    

