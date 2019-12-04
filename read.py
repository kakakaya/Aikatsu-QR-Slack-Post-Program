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
import sys
from urllib import request
import access

SLACK_BOT_TOKEN = access.SLACK_BOT_TOKEN

aat = access.access_token

client = slack.WebClient(token=SLACK_BOT_TOKEN)

def get_shortenURL(longUrl):
    url = 'https://api-ssl.bitly.com/v3/shorten'
    access_token = aat
    query = {
            'access_token': access_token,
            'longurl':longUrl
            }
    r = requests.get(url,params=query).json()
    return r

def post():
    response = client.chat_postMessage(
    channel=Slackch,text=(card)
    )

while True:
    print("アイカツQRコードSlack送信システム")
    print('該当の画像を入れてください')

    path = input()

    if ".com" not in path:
        if ".jp" not in path:
            if ".jpg" not in path:
                if ".jpeg" not in path:
                    print("これ画像じゃないですよね...")
                    print("再実行しますか？[Y/N]")
                    retry = input()
                    if 'Y' in retry or 'Yes' in retry or 'yes' in retry or 'y' in retry or 'YES' in retry:
                        continue
                    elif 'N' in retry or 'No' in retry or 'no' in retry or 'n' in retry or 'NO' in retry:
                        break
                    else:
                        print("リトライしてください")
                        continue
        
    else:
        pass

    if "com" in path or "jp" in path and "jpg" not in path and "jpeg" not in path:
        print("画像ダウンロード開始...")
        try:
            URL = path
        except ValueError:
            print("不正なURLでは？？？")
            print("再実行しますか？[Y/N]")

            retry = input()
            if 'Y' in retry or 'Yes' in retry or 'yes' in retry or 'y' in retry or 'YES' in retry:
                    continue
            elif 'N' in retry or 'No' in retry or 'no' in retry or 'n' in retry or 'NO' in retry:
                    break
            else:
                print("リトライしてください")
                continue
        try:
            request.urlretrieve(URL, "python.jpg")
        except ValueError:
            print("不正なURLでは？？？")
            print("再実行しますか？[Y/N]")

            retry = input()
            if 'Y' in retry or 'Yes' in retry or 'yes' in retry or 'y' in retry or 'YES' in retry:
                    continue
            elif 'N' in retry or 'No' in retry or 'no' in retry or 'n' in retry or 'NO' in retry:
                    break
            else:
                print("リトライしてください")
                contunue
        path = "python.jpg"
        print("画像ダウンロード終了...")
    
    try:
        data = decode(Image.open(path))
    except FileNotFoundError:
        print("本当にそこにありますか？？？")
        print("再実行しますか？[Y/N]")
        retry = input()
        if 'Y' in retry or 'Yes' in retry or 'yes' in retry or 'y' in retry or 'YES' in retry:
                    continue
        elif 'N' in retry or 'No' in retry or 'no' in retry or 'n' in retry or 'NO' in retry:
                    break
        else:
            print("リトライしてください")
            continue
                    
    path = data[0][0].decode('utf-8', 'ignore')

    print(path)

    path = get_shortenURL(path)

    print(path)
    
    card = path['data']['url']
    
    post()
    
    path= "none"
