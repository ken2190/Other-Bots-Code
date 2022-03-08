#Author: Nikola Gavric

#This code gives however many upvotes is needed on coinmooner
#Not fully finished as you manually need to enter the coinID inside of data but can easily to automated to retreive coinID from url 

import requests
import aiohttp

#Vote api link
url = "https://coinmooner.com/api/voting/"

#Data to post
data ={
    'operationName': 'UpvoteCoin',
    'variables': {
        'coinId': '12773',
    },
    'query': 'mutation UpvoteCoin($coinId: String!, $captcha: String) {\n  upvoteCoin(coinId: $coinId, captcha: $captcha)\n}\n',
}

#Header to post
headers = {
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4725.189 Safari/537.36'
} 


amount_of_votes = int(input("Enter amount of upvotes: ))
                            
for i in range(amount_of_votes):
  #Get proxy from proxy list
  f=open('proxies.txt')
  lines=f.readlines()
  list = lines[i]
  list = list.split(":")
  #Reformat proxy
  proxy1 = list[0] + ":" + list[1]
  auth1 = list[2]
  auth2 = list[3]
  auth2 = auth2.rstrip("\n")
  proxy1 = auth1 + ":" + auth2 + "@" + proxy1
  proxies = {
  "http" : "http://" + proxy1,
  "https":"http://" + proxy1,

  }
  
  #Post
  r = requests.post(url, proxies = proxies, headers = headers, json = data)
  print(f"Upvotes: {i}     {r.text}")
