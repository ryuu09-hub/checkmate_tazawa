#!/usr/bin/env python
#! -*- coding: utf-8 -*-
from keras.preprocessing import image
from keras.models import load_model
from keras.preprocessing.image import img_to_array
import pygame.mixer
import numpy as np
import picamera
from PIL import Image
from time import sleep
import time

photo_filename = '/tmp/data.jpg'

def shutter():
    photofile = open(photo_filename, 'wb')
    print(photofile)

    # pi camera 用のライブラリーを使用して、画像を取得
    with picamera.PiCamera() as camera:
        #camera.resolution = (640,480)
        camera.resolution = (300,400)
        camera.start_preview()
        sleep(1.000)
        camera.capture(photofile)

if __name__ == '__main__':
    # モデル+重みを読込み
    #self_model = load_model('MobileNet_auto_fine3_150_3.h5')
    self_model = load_model('mobilenetv2_for_2class.h5')

    # 音声ファイル初期化
    pygame.mixer.init()
    pygame.mixer.music.load("Cash_Register-Beep01-1.mp3")

    # 正解ラベル
    label =  ['fantagrape','ayataka']
    # 商品価格
    money = {'fantagrape':120,'ayataka':135}
    
    #初期メモリ確保
    temp_photo='0.jpg'
    img = Image.open(temp_photo)
    img = img.resize((224, 224))
    img_array = img_to_array(img)
    img_array = img_array.astype('float32')/255.0
    img_array = img_array.reshape((1,224,224,3))
    #最初の推定（時短）
    img_pred = self_model.predict(img_array)


    while True:
        money_sum = 0
        key = input('商品をスキャンする場合は「Enter」を押して下さい')
        while True:
            # 画像の取得
            shutter()
            
            # 音声再生
            pygame.mixer.music.play(1)
            sleep(1)
            # 再生の終了
            pygame.mixer.music.stop()
            
            # 画像をモデルの入力用に加工
            img = Image.open(photo_filename)
            #img = Image.open("./0.jpg")
            img = img.resize((224, 224))
            img_array = img_to_array(img)
            img_array = img_array.astype('float32')/255.0
            img_array = img_array.reshape((1,224,224,3))

            # predict
            #タイムを計測
            start = time.time()
            img_pred = self_model.predict(img_array)
            process_time=time.time() - start
            print('処理時間：{:.3f}秒'.format(process_time))
            if process_time >=2.0:
                print('処理時間がかかり過ぎます。')
                continue
            print("debug:",img_pred)
            
            if np.max(img_pred) < 0.10:
                key = input('登録外の商品です。「Enter」を押しもう一度スキャンをして下さい。')
                continue

            name = label[np.argmax(img_pred)]
            print(name)
            money_sum += money[name]
            print("小計",money_sum)

            key = input('続けて商品をスキャンする場合は「y」,会計する場合は「Enter」,キャンセルする場合は「c」を押してください。')
            if key == 'c':
                print("商品はキャンセルされました。")
                break
            elif key != 'y':
                print("合計:{}円".format(money_sum))
                break

