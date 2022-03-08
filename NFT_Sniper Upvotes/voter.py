#Author: Nikola Gavric

#This code asks user for their project link and gives them however many upvotes they need

#Imports
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import names
import string
import time
import random
from mail import main
from selenium.webdriver.common.by import By
from threading import Thread

#Selenium options
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--window-size=650,650")

link = = str(input("Enter your nftsniper.net link: ))
amount_of_upvotes = int(input("How many upvotes do you need? "))

for i in range(amount_of_upvotes):
    #define selenium driver
    driver = webdriver.Chrome(options=chrome_options)

    #Get username and apssword from accounts.txt
    f=open('accounts.txt')
    lines=f.readlines()
    email_pass = lines[i]
    email_pass = email_pass.split(":")
    email = email_pass[0]
    password = email_pass[1]

    #Go to NFTSniper.net
    driver.get("https://nftsniper.net/login")

    #Login
    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.NAME, "password").send_keys(password)
    #driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div[2]/div/form/div[4]/button").click()
    
    #Go to link
    driver.get(link)
                   
    #Click upvote
    time.sleep(5)
    try:
        driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div[2]/div[1]/div[2]/div[3]/div/div/span[2]/a").click()
    except:
        print(f"There was a problem upvoting on this account: {email}")

    print(f"Upvoted: {i}")
    driver.close()
