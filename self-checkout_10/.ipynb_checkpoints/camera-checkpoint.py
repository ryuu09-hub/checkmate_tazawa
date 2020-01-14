import picamera
from time import sleep

photo_filename = '/data_pi'

# pi camera 用のライブラリーを使用して、画像を取得
for i in range(20):
    with picamera.PiCamera() as camera:
        camera.resolution = (300,400)
        camera.start_preview()
        sleep(5)
        camera.capture("{}/image_{}.jpg".format(photo_filename,i))
        camera.stop_preview()
