from flask import Flask, send_file, request, jsonify
from json import loads
from time import sleep
from src.text_to_speech import speak
# from src.motor import rotateMotor
# from src.camera import Camera
from src.image_to_txt import Image_to_Text
from re import compile, split

app = Flask(__name__,
            template_folder='public', static_folder='public', static_url_path='')
last_paragraph = None
counter = 0


@app.route("/")
def index():
    return send_file('public/index.html')


@app.route("/save", methods=['GET'])
def save_page():
    global last_paragraph
    with open('./assets/captured_text/{}.txt'.format(counter), 'w') as file:
        file.write(last_paragraph)
    return '', 204


@app.route("/page", methods=['POST'])
def get_page():
    global counter, last_paragraph, camera, drive
    counter += 1
    # rotateMotor(0, 2, 120, 600)
    sleep(1.5)
    # camera.capture()
    # last_paragraph = drive.image2text('./assets/temp.jpg')
    last_paragraph = drive.image2text('./assets/electromagnetics.png')
    return jsonify({'page': last_paragraph})


@app.route("/read", methods=['GET', 'POST'])
def read_page():
    if last_paragraph:
        global sep
        lines = split(sep, last_paragraph)
        currIdx = 0
        line = ''
        while currIdx < len(lines):
            while currIdx < len(lines) and len(line + lines[currIdx]) < 198:
                line += lines[currIdx] + ' '
                currIdx += 1
            print(line)
            speak(line)
            line = ''
    return '', 204

@app.route("/up", methods=['POST'])
def moveUp()
    # Move board up (angle -> bigger)
    return

@app.route("/down", methods=['POST'])
def moveDown()
    # Move board down (angle -> smaller)
    return

if __name__ == "__main__":
    drive = Image_to_Text()
    camera = None
    # camera = Camera()
    sep = compile(r'[,.]\s')
    app.run()
