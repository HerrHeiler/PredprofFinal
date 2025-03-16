from flask import Flask, request
import requests, json

token = 'wAruBW'

def get_tile():
    pageURL = "https://olimp.miet.ru/ppo_it/api"
    req = requests.get(pageURL)
    return json.loads(req.content.decode("UTF-8"))["message"]["data"]

def tiles_to_files():
    sp = []
    while len(sp) != 16:
        tile = get_tile()
        if tile in sp:
            continue
        sp.append(tile)
    with open("tiles.json", "w") as f:
        json.dump(sp, f, indent=4)
# tiles_to_files()
with open("tiles.json", "r") as f:
    sp = json.load(f)
lines = []
tiles = []
on_their_places = []
for first_index in range(len(sp)):
    main_tile = sp[first_index]
    verh, niz, levo, pravo = -1, -1, -1, -1
    for second_index in range(len(sp)):
        temp_tile = sp[second_index]
        if main_tile[0] == temp_tile[-1]:
            verh = second_index
        if main_tile[-1] == temp_tile[0]:
            niz = second_index
        f = True; i = 0
        while i != 64 and f:
            if main_tile[i][0] != temp_tile[i][-1]:
                f = False
            i += 1
        if f: levo = second_index
        f = True; i = 0
        while i != 64 and f:
            if main_tile[i][-1] != temp_tile[i][0]:
                f = False
            i += 1
        if f: pravo = second_index
    if pravo != -1 and levo == -1 and verh != -1 and niz == -1:
        first = main_tile
def next_tile(tile):
    for second_index in range(len(sp)):
        temp_tile = sp[second_index]
        i = 0
        f = True
        pravo = -1
        while i != 64 and f:
            if tile[i][-1] != temp_tile[i][0]:
                f = False
            i += 1
        if f: pravo = second_index
    return pravo
def below_tile(tile):
    for second_index in range(len(sp)):
        temp_tile = sp[second_index]
        if tile[-1] == temp_tile[0]:
            niz = second_index
    return niz
i = 0
tiles = [main_tile]
ans = ""
while i != 16:
    temp_tile = tiles[-1]
    ans += str(tiles[-1])
    if i % 8 != 7:
        ans += "\n"
        tiles.append(next_tile(temp_tile))
    else:
        tiles.append(below_tile(temp_tile))
    i += 1
    print(tiles)
with open("answer.txt", "w") as f:
    f.write(ans)