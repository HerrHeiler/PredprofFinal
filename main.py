from flask import Flask, request
import requests, json

token = 'wAruBW'

pageURL = "https://olimp.miet.ru/ppo_it/api"
req = requests.get(pageURL)
print(len(json.loads(req.content.decode("UTF-8"))["message"]["data"]))
