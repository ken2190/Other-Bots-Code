#Author: Nikola Gavric

#This code generates accounts on nftsniper.net

#Imports
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import names
import string
import time
import random
from mail import main
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


#Selenium driver options
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_extension('adblock.crx')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--window-size=700,700")

#Register page url
url = "https://nftsniper.net/register"


#Generate password function
def get_random_string(length):
# choose from all lowercase letter
  letters = string.ascii_lowercase
  result_str = ''.join(random.choice(letters) for i in range(length))
  return result_str

amount_of_accounts = int(input("How many accounts would you like to create?"))

for i in range(amount_of_accountss):
  
  #Create driver
  driver = webdriver.Chrome(options=chrome_options)
  
  #generate name and password
  name = (names.get_full_name())
  number = random.randint(1,20)
  number = str(number)
  password = get_random_string(10)
  password = password+number
  driver.get(url)

  time.sleep(5)
  
  #Close adblock install window once installed
  driver.switch_to.window(driver.window_handles[1])
  driver.close()
  driver.switch_to.window(driver.window_handles[0])
  
  #Generate email adress
  main()

  #Get email address from txt file
  with open('emails.txt', 'r') as f:
    lines = f.read().splitlines()
    email = lines[-1]
  email = str(email)

  #Record email and password in accounts.txt
  file = open("accounts.txt", "a" )
  file.write(email + ':' + password + '\n')
  file.close()

  #Create account
  driver.find_element(By.NAME, "name").send_keys(name)
  driver.find_element(By.NAME, "email").send_keys(email)
  driver.find_element(By.NAME, "password").send_keys(password)
  driver.find_element(By.NAME, "password_confirmation").send_keys(password)
  driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div[2]/div/form/div[5]/button").click()
  x = email.split("@")
  
  #Go to email url to verify account
  driver.get(f'https://www.1secmail.com/?login={x[0]}&domain={x[1]}')
  
  #Keep searching for verification link until it shows up
  found = False
  while found is False:
    try:
      iframe = driver.find_element(By.XPATH, "//*[@id='messageiframe']")
      driver.switch_to.frame(iframe)
      driver.find_element(By.XPATH, "/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/a")
      break
      found = True
    except:
      try:
        driver.find_element(By.XPATH, "/html/body/div/div[4]/div[4]/div/table/tbody/tr[2]/td[2]/a").click()
      except:
        print("Retrying")
        
  #Click verification link
  driver.find_element(By.XPATH, ("/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/a")).click()
  
  time.sleep(3)
  print(f"created account: {i}")
  driver.close()
