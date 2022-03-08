#Author: Nikola Gavric

#This code generates however many watchlists are needed for a specific coin

import requests

#header to post
headers = {
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
} 

amount_of_watchlists = int(input("How many watchlists do you need? "))

for i in range(amount_of_watchlists):
    #Create requests session
    s = requests.Session()
    
    #Get account from accounts.txt
    f=open('accounts.txt')
    lines=f.readlines()
    email_pass = lines[i]
    email_pass = email_pass.split(":")
    email = email_pass[0]
    password = email_pass[1]
    

    #Get proxy from list
    f1=open('proxy_list.txt')
    lines1=f1.readlines()
    list = lines1[i]
    list = list.split(":")
    proxy1 = list[0] + ":" + list[1]
    auth1 = list[2]
    auth2 = list[3]
    #Reformat proxies
    auth2 = auth2.rstrip("\n")
    proxy1 = auth1 + ":" + auth2 + "@" + proxy1
    proxies = {
      "http" : "http://" + proxy1,
      "https":"http://" + proxy1,
    }

    #Data for login post
    data = {
      "email":email,
      "password":password,
      "platform":"web","token":"captcha#8e2fe9272e074e0990986bdd8215e20e-kPSK4mouxDG6ZttejvUGkHKgXzEsYMjbf6B5fIBZqutgNnJl"}
    
    #Login post
    url = "https://api.coinmarketcap.com/auth/v4/user/login"
    r = s.post(url, proxies = proxies, headers = headers, json = data)
    print(r.status_code)


    #Data to post for watchlist
    data = {
    "resourceId":2280,
    "resourceType":"CRYPTO",
    "subscribeType":"SUBSCRIBE"
    }

     #Wathclist post
    r1 = s.post(url, proxies = proxies, headers = headers, json = data)
    print(r1.status_code)
