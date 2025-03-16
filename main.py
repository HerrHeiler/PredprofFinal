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
ans = {}
for index in range(len(sp)):
    tile = sp[index]
    if sum(tile[0]) >= 15300:
        i = 0; s = 0; s2 = 0
        while i != 64:
            s += tile[i][0]
            s2 += tile[i][-1]
            i += 1
        if s >= 15300:
            first = tile
            tiles.append(first)
            sp.pop(index)
            break
for index in range(len(sp)):
    tile = sp[index]
    if sum(tile[0]) >= 15300:
        i = 0; s1 = 0
        while i != 64:
            s1 += tile[i][0]
            i += 1
        if abs(s1 - s2) <= 640:
            second = tile
            tiles.append(second)
            sp.pop(index)
            break
for index in range(len(sp)):
    tile = sp[index]
    if sum(tile[0]) >= 15300:
        i = 0; s1 = 0
        while i != 64:
            s1 += tile[i][0]
            i += 1
        if s1 < 15300:
            third = tile
            tiles.append(third)
            sp.pop(index)
            break
# 4
for index in range(len(sp)):
    tile = sp[index]
    if sum(tile[0]) >= 15300:
        tiles.append(tile)
        sp.pop(index)
        break
# 5
for index in range(len(sp)):
    tile = sp[index]
    i = 0; s1 = 0
    while i != 64:
        s1 += tile[i][0]
        i += 1
    if s1 >= 15300:
        if abs(sum(tile[0]) - sum(first[-1])) < 640:
            tiles.append(tile)
            sp.pop(index)
            break
# 6
for index in range(len(sp)):
    tile = sp[index]
    if tile[-1][-1] == 0 and tile[-1][-2] == 0 and tile[-1][-3] == 0 and tile[-2][-1] == 0 and tile[-2][-2] == 0:
        tiles.append(tile)
        sp.pop(index)
        break
# 7
for index in range(len(sp)):
    tile = sp[index]
    if tile[-1][0] == 0 and tile[-1][1] == 0 and tile[-1][2] == 0 and tile[-2][0] == 0 and tile[-2][1] == 0:
        tiles.append(tile)
        print("7")
        sp.pop(index)
        break
# 8
for index in range(len(sp)):
    tile = sp[index]
    i = 0; s1 = 0
    while i != 64:
        s1 += tile[i][-1]
        i += 1
    if s1 >= 15300:
        if abs(sum(tile[0]) - sum(tiles[3][-1])) < 640:
            tiles.append(tile)
            print("8")
            sp.pop(index)
            break
# 9
for index in range(len(sp)):
    tile = sp[index]
    i = 0; s1 = 0
    while i != 64:
        s1 += tile[i][0]
        i += 1
    if s1 >= 15300 and sum(tile[-1]) < 15300:
        tiles.append(tile)
        sp.pop(index)
        break
# 10
for index in range(len(sp)):
    tile = sp[index]
    if tile[0][-1] == 0 and tile[0][-2] == 0 and tile[0][-3] == 0 and tile[0][-1] == 0 and tile[0][-2] == 0:
        tiles.append(tile)
        sp.pop(index)
        break
# 11
for index in range(len(sp)):
    tile = sp[index]
    if tile[0][0] == 0 and tile[0][1] == 0 and tile[0][2] == 0 and tile[0][0] == 0 and tile[0][1] == 0:
        tiles.append(tile)
        sp.pop(index)
        break
# 12
for index in range(len(sp)):
    tile = sp[index]
    i = 0; s1 = 0
    while i != 64:
        s1 += tile[i][-1]
        i += 1
    if s1 >= 15300 and sum(tile[-1]) < 15300:
        tiles.append(tile)
        sp.pop(index)
        break
# 13
for index in range(len(sp)):
    tile = sp[index]
    i = 0; s1 = 0
    while i != 64:
        s1 += tile[i][0]
        i += 1
    if s1 >= 15300:
        tiles.append(tile)
        sp.pop(index)
        break
# 14
for index in range(len(sp)):
    tile = sp[index]
    if sum(tile[-1]) >= 15300 and abs(sum(tile[0]) - sum(tiles[9][-1])) < 640:
        tiles.append(tile)
        sp.pop(index)
        break
# 15
for index in range(len(sp)):
    tile = sp[index]
    i = 0; s1 = 0
    while i != 64:
        s1 += tile[i][-1]
        i += 1
    if s1 < 15300 and sum(tile[-1]) > 15300:
        tiles.append(tile)
        sp.pop(index)
        break
tiles.append(sp[0])
def next_tile(tile):
    for index in range(len(sp)):
        temp_tile = sp[index]
        i = 0
        s1 = 0; s2 = 0
        while i != 64:
            s1 += tile[i][-1]
            s2 += temp_tile[i][0]
            i += 1
        if abs(s1-s2):
            sp.pop(index)
            return temp_tile

# def below_tile(tile):
#     for index in range(len(sp)):
#         temp_tile = sp[index]
#         if abs(sum(tile[-1]) - sum([temp_tile[]])):
#             sp.pop(index)
#             return temp_tile


ans = str(tiles)
with open("answer.txt", "w") as f:
    f.write(ans)
