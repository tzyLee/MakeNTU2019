from text_to_speech import speak
from image_to_txt import image2text
from camera import capture

def main():
    capture(duration = 10)
    print("Image captured")
    res = image2text('../assets/capture.png')[20:200]
    speak(res)


if __name__ == "__main__":
    main()
