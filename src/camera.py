from picamera import PiCamera
from time import sleep


def capture(duration=5):
    camera = PiCamera()
    camera.start_preview()
    sleep(duration)
    camera.capture('../assets/capture.png')
    camera.stop_preview()


class Camera:
    def __init__(self, save_dir='../assets/'):
        self.camera = PiCamera()
        self.save_dir = save_dir

    def __del__(self):
        self.camera.close()

    def capture(self, file_name='temp.jpg'):
        self.camera.capture(save_dir+file_name)
