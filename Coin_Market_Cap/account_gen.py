#Author: Nikola Gavric

#This code generates accounts for CoinMarketCap

import requests
from mail import main
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import random
import string
import time

#Signup api site
url = "https://api.coinmarketcap.com/auth/v4/user/signUp"

#Selenium options
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--single-process')
chrome_options.add_extension('adblock.crx')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument("--window-size=700,700")

#Header for post
headers = {
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
} 

#Generate password function
def get_random_string(length):
  # choose from all lowercase letter
  letters = string.ascii_lowercase
  result_str = ''.join(random.choice(letters) for i in range(length))
  return result_str

amount_of_accounts = int(input("How many accounts do you need? "))
                               
for i in range(amount_of_)accounts):
    #Generate email
    main()

    #Get email from txt file
    with open('emails.txt', 'r') as f:
        lines = f.read().splitlines()
        email = lines[-1]
    email = str(email)

    #Generate password
    number = random.randint(1,20)
    number = str(number)
    password = get_random_string(10)
    password = password+number

    #Record email and password for account in accounts.txt
    file = open("accounts.txt", "a" )
    file.write(email + ':' + password + '\n')
    file.close()

    #Data to post to CoinMArketCap
    data = {
        "email":email,
        "password":password,
        "newsletter": 'false',
        "token":"captcha#809f58f48f7d4f4e874d3c969a9a77e2-wlViZBNQJVizzrmy2wIIIFJbW4si7PFJiRX2XdGiC29nozt6",
        "name":email,
        "platform":"web",
        "privacy":'true',
        "referralCode":""
        } 

    #Get proxy from list
    f=open('proxy_list.txt')
    lines=f.readlines()
    list = lines[i]
    list = list.split(":")
    #Change proxy format
    proxy1 = list[0] + ":" + list[1]
    auth1 = list[2]
    auth2 = list[3]
    auth2 = auth2.rstrip("\n")
    proxy1 = auth1 + ":" + auth2 + "@" + proxy1
    proxies = {
    "http" : "http://" + proxy1,
    "https":"http://" + proxy1,
    }  
    
    #Post data to signup api
    r = requests.post(url, proxies = proxies, headers = headers, json = data)


  #Verify account using Selenium
  #Get email inbox url from txt file
    wire_options = {
        'proxy': {
        'http': 'http://' + proxy1,
        'https': 'https://' + proxy1,
        }
    }
    
    #Set selenium driver
    driver = webdriver.Chrome(options=chrome_options, seleniumwire_options= wire_options)
    
    #Get mail inbox url
    x = email.split("@")
    #Go to mail inbox url
    driver.get(f'https://www.1secmail.com/?login={x[0]}&domain={x[1]}')

    #Keep checking for verification link until it arrives
    found = False
    while found is False:
      try:
        iframe = driver.find_element(By.XPATH, "//*[@id='messageiframe']")
        driver.switch_to.frame(iframe)
        driver.find_element(By.XPATH, "/html/body/div/table/tbody/tr/td/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[7]/td/span/a")
        break
        found = True
      except:
        try:
          driver.find_element(By.XPATH, "/html/body/div/div[4]/div[4]/div/table/tbody/tr[2]/td[2]/a").click()
        except:
          print("Retrying")

  #Click on verification link
    driver.find_element(By.XPATH, ("/html/body/div/table/tbody/tr/td/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[7]/td/span/a")).click()
    time.sleep(3)

  #Erase email adress from txt file
    file = open("emails.txt","r+")
    file.truncate(0)
    file.close()

    print(f"Account Created: {i}")
