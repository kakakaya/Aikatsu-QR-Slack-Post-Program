# -*- coding: UTF-8 -*-
from pyzbar.pyzbar import decode
from PIL import Image
import os
import slack
import requests
import json
import pprint
import time
import urllib
from urllib import request
import access

rico = 'none'

SLACK_BOT_TOKEN = access.SLACK_BOT_TOKEN

att = access.access_token

client = slack.WebClient(token=SLACK_BOT_TOKEN)

def get_shortenURL(longUrl):
    url = 'https://api-ssl.bitly.com/v3/shorten'
    access_token = att
    query = {
            'access_token': access_token,
            'longurl':longUrl
            }
    r = requests.get(url,params=query).json()
    return r

def post():
    response = client.chat_postMessage(
    channel='#学習用チャンネル',text=(aikatsu)
    )

while True:
    print("アイカツQRコードSlack送信システム")
    print('該当の画像を入れてください')

    rico = input()

    if ".com" not in rico:
        if ".jp" not in rico:
            if ".jpg" not in rico:
                if ".jpeg" not in rico:
                    print("これ画像じゃないですよね...")
                    print("再実行しますか？[Y/N]")
                    arisa = input()
                    if 'Y' in arisa or 'Yes' in arisa or 'yes' in arisa or 'y' in arisa or 'YES' in arisa:
                        continue
                    elif 'N' in arisa or 'No' in arisa or 'no' in arisa or 'n' in arisa or 'NO' in arisa:
                        break
                    else:
                        print("リトライしてください")
                        continue
        
    else:
        pass

    if "com" in rico or "jp" in rico and "jpg" not in rico and "jpeg" not in rico:
        print("画像ダウンロード開始...")
        try:
            URL = rico
        except ValueError:
            print("不正なURLでは？？？")
            print("再実行しますか？[Y/N]")
            arisa = input()
            if 'Y' in arisa or 'Yes' in arisa or 'yes' in arisa or 'y' in arisa or 'YES' in arisa:
                    continue
            elif 'N' in arisa or 'No' in arisa or 'no' in arisa or 'n' in arisa or 'NO' in arisa:
                    break
            else:
                print("リトライしてください")
                continue
        try:
            request.urlretrieve(URL, "python.jpg")
        except ValueError:
            print("不正なURLでは？？？")
            print("再実行しますか？[Y/N]")
            arisa = input()
            if 'Y' in arisa or 'Yes' in arisa or 'yes' in arisa or 'y' in arisa or 'YES' in arisa:
                    continue
            elif 'N' in arisa or 'No' in arisa or 'no' in arisa or 'n' in arisa or 'NO' in arisa:
                    break
            else:
                print("リトライしてください")
                continue
        rico = "python.jpg"
        print("画像ダウンロード終了...")
    
    try:
        data = decode(Image.open(rico))
    except FileNotFoundError:
        print("本当にそこにありますか？？？")
        print("再実行しますか？[Y/N]")
        arisa = input()
        if 'Y' in arisa or 'Yes' in arisa or 'yes' in arisa or 'y' in arisa or 'YES' in arisa:
            continue
        elif 'N' in arisa or 'No' in arisa or 'no' in arisa or 'n' in arisa or 'NO' in arisa:
            break
        else:
            print("リトライしてください")
            continue
                    
    rico = data[0][0].decode('utf-8', 'ignore')

    print(rico)

    rico = get_shortenURL(rico)

    print(rico)

    with open('read.json', 'w') as d:
        json.dump(rico, d, ensure_ascii=False)

    with open('read.json', 'r') as f:
        jsn = json.load(f)
        aikatsu = (jsn['data']['url'])

    post()
    
    rico = "none"
