from text_to_speech import speak
from image_to_txt import Image_to_Text
from camera import capture


def main():
    drive = Image_to_Text()
    capture(duration=10)
    print("Image captured")
    res = drive.image2text('../assets/capture.png')[20:200]
    speak(res)


if __name__ == "__main__":
    main()
