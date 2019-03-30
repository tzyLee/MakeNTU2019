from src.text_to_speech import speak
from src.image_to_txt import Image_to_Text


def main():
    drive = Image_to_Text()
    res = drive.image2text('./assets/electromagnetics.png')
    a = res[20:120]
    print(a)
    speak(a)


if __name__ == "__main__":
    main()
