from flask import Flask, send_file, request, jsonify
from json import loads
from time import sleep
from src.text_to_speech import speak, speekLock
# from src.motor import rotateMotor
# from src.camera import Camera
from src.image_to_txt import Image_to_Text
from re import compile, split
from threading import Thread

app = Flask(__name__,
            template_folder='public', static_folder='public', static_url_path='')
last_paragraph = None
lines = None
counter = 0


@app.route("/")
def index():
    return send_file('public/index.html')


@app.route("/save", methods=['GET'])
def save_page():
    if not last_paragraph:
        return '', 404
    with open('./assets/captured_text/{}.txt'.format(counter), 'w') as file:
        file.write(last_paragraph)
    return '', 204


@app.route("/page", methods=['POST'])
def get_page():
    global counter, last_paragraph, camera, drive, sep, lines
    counter += 1
    # rotateMotor(0, 2, 120, 600)
    # sleep(1.5)
    # camera.capture()
    # last_paragraph = drive.image2text('./assets/temp.jpg')

    last_paragraph = drive.image2text('./assets/electromagnetics.png')
    lines = split(sep, last_paragraph)
    return jsonify({'page': last_paragraph})


@app.route("/read", methods=['POST'])
def read_page():
    global speekLock
    if not speekLock.acquire():
        return '', 403
    data = loads(request.data)
    lastIdx, currIdx = data['lastIdx'], data['lineIdx']
    acc_len = 0
    # `lastIndex` sent from here last time
    if last_paragraph:
        if currIdx >= len(lines):  # had read once before
            speekLock.release()
            return '', 200  # finished reading
        line = []
        if currIdx < len(lines):
            while currIdx < len(lines) and acc_len + len(lines[currIdx]) < 198:
                line.append(lines[currIdx])
                acc_len += len(lines[currIdx])
                currIdx += 1
            acc_len += 2*len(line)  # add length of separator
            line = ''.join(line)
            print(line)
            t = Thread(target=speak, args=(line,))  # start a thread to speak
            t.start()
    else:
        currIdx = 0  # TODO is this 206?
        lastIdx = 0
        speekLock.release()
    # To be continued
    return jsonify({'lineIdx': currIdx, 'lastIdx': lastIdx + acc_len}), 206


if __name__ == "__main__":
    drive = Image_to_Text()
    camera = None
    # camera = Camera()
    sep = compile(r'[,.]\s')
    app.run()
