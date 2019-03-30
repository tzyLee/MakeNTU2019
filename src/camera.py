from picamera import PiCamera
from time import sleep

def capture(duration = 5):
    camera = PiCamera()
    camera.start_preview()
    sleep(duration)
    camera.capture('../assets/capture.png')
    camera.stop_preview()

