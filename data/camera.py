import picamera
from time import sleep

photo_filename = 'data_pi'

# pi camera 用のライブラリーを使用して、画像を取得
while True:
    key = input("商品名選択,いちご「i」,オランジーナ「o」,ファンタ「f」,\
カルピス「k」,もも「m」,VitaminWater「v」,あやたか「g」,\
ペプシコーラ「p」,amino「a」, water「w」")
    drink ={"i":"ichigo","o":"orangena","f":"fantagrape","c":"calpis","m":"momo","v":"VitaminWater",
            "g":"ayataka","p":"pepsi","a":"amino_supli","w":"water_g"}
    for i in range(30):#20枚撮影
        with picamera.PiCamera() as camera:
            camera.resolution = (300,400)
            camera.start_preview()
            sleep(5)
            camera.capture("{}/{}/image5_{}.jpg".format(photo_filename,drink[key],i))
            camera.stop_preview()
            
    if key == 'o':
        key = input("もう一つのサンプルを取得します。準備できたら「Enter」")
        for i in range(60):#20枚撮影
            with picamera.PiCamera() as camera:
                camera.resolution = (300,400)
                camera.start_preview()
                sleep(5)
                camera.capture("{}/{}/image_{}.jpg".format(photo_filename,drink[key],i))
                camera.stop_preview()
