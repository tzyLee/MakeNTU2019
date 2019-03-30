from src.text_to_speech import speak
from src.image_to_txt import image2text


def main():
    res = image2text('./assets/electromagnetics.png')
    a = res[20:120]
    print(a)
    speak(a)


if __name__ == "__main__":
    main()
