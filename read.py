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
import key
import cv2
import pyzbar.pyzbar as pyzbar
import PIL.Image

SLACK_BOT_TOKEN = key.SLACK_BOT_TOKEN

aat = key.access_token

slackch = key.slackch

client = slack.WebClient(token=SLACK_BOT_TOKEN)

def SearchImage():
  homeDir = expanduser('~')
  imageDir = homeDir + '\\Pictures\\Camera Roll'
  imageList = os.listdir(imageDir)
  return (imageDir + '\\' + imageList[-1])

def QRreade(image):
  readResult = decode(Image.open(image))
  if (readResult != []):
    return readResult
  else:
    print('QRコードを検出できませんでした')
    exit()

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
    channel=slackch,text=card
    )
    
print("アイカツQRコードSlack送信システム")
print('該当の画像があるパスまたはURLを入れてください')
print("QRを読み取る場合はQR-Readと入れてください")
print("カメラが起動します")
print("終了する場合はexitまたはCtrl+Dでお願いします")

while True:
    path = input()

    if "exit" in path:
        exit()

    if ".com" not in path:
        if ".jp" not in path:
            if ".jpg" not in path:
                if ".jpeg" not in path:
                    if "QR" not in path:
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
    
    if "QR-Read" in path:
            window_name = "main"
            cap = cv2.VideoCapture(0)
            cap.set(3, 1280)
            cap.set(4, 720)
            cap.set(5, 15)
            cv2.namedWindow(window_name)
        
            while True:
                ret, flame = cap.read()
                cv2.imshow(window_name, flame)
                tresh = 100
                max_pixel = 255
                ret, flame = cv2.threshold(flame, tresh, max_pixel, cv2.THRESH_BINARY)
                qr_result = pyzbar.decode(flame)
                if qr_result != []:
                    print(qr_result[0][0])
                    if "http://aikatsu.com/qr/id=" in qr_result:
                        print("旧カツのカードは対応していません。別のカードを読み込んでください。")
                        print("該当の画像を入れてください")
                        print("終了する場合はexitまたはCtrl+Dでお願いします")
                        path = "none"
                        continue
                    qr_result = qr_result[0][0].decode('utf-8', 'ignore')
                    break
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        
    cv2.destroyAllWindows()

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
        image = "python.jpg"
        print("画像ダウンロード終了...")
      
    path = path.strip()
    
    try:
        read = decode(Image.open(path))
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
            
    path = read[0][0].decode('utf-8', 'ignore')
    
    print(path)

    path = get_shortenURL(path)

    print(path)
    
    try:
        card = path['data']['url']
    except TypeError:
        print("旧カツカードまたは読み込めない形式のカードです、別のカードを読み込んでください。")
        print("該当の画像を入れてください")
        print("終了する場合はexitまたはCtrl+Dでお願いします")
        path = "none"
        continue
        
    post()
    
    card = "none"
    
    image = "none"
    
    path = "none"
    
    print("該当の画像を入れてください")
    print("終了する場合はexitまたはCtrl+Dでお願いします")