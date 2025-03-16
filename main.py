from flask import Flask, request
import requests, json

token = 'wAruBW'
sp = []
pageURL = "https://olimp.miet.ru/ppo_it/api"
req = requests.get(pageURL)
# print(json.loads(req.content.decode("UTF-8"))["message"]["data"])

for i in range(30):
    req = requests.get(pageURL)
    a = json.loads(req.content.decode("UTF-8"))["message"]["data"]
    if a not in sp:
        sp.append(a)
        print(a)
