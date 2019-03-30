from googletrans.gtoken import TokenAcquirer
import vlc
import sys
from time import sleep
from urllib.parse import quote
from threading import Lock

speekLock = Lock()
vlc_instance = vlc.Instance()
player = vlc_instance.media_player_new()


def get_len(string):
    a = string.split(' ')
    return len(a)


def get_token(string):
    acquirer = TokenAcquirer()
    tk = acquirer.do(string)
    return tk


def to_utf8(string):
    stirng = string.encode('utf8')
    return str(string).replace('\\', '%')[2:]


def language(string):
    if string[0] >= u'\u4e00' and string[0] <= u'\u9fa5':
        return 'zh_CN'
    else:
        return 'en'


def speak(string):
    global player
    url = 'http://translate.google.com.tw/translate_tts?ie=UTF-8&q={string}&tl={lang}&total=1&idx=0&textlen={len}&tk={token}&client=webapp&prev=input'.format(string=quote(string), lang=language(
        string), len=get_len(string), token=get_token(string))
    # url = 'https://translate.google.com.tw/translate_tts?ie=UTF-8&q=%E8%B6%95%E7%BE%9A%E7%BE%8A&tl=zh-CN&total=1&idx=0&textlen=3&tk=353679.254520&client=t&prev=input&ttsspeed=0.24'
    # print('The url is:', url)
    player.set_mrl(url)
    player.play()
    sleep(1.5)
    duration = player.get_length() // 1000
    sleep(duration + 0.5)
    speekLock.release()


if __name__ == '__main__':
    # speak('Finally, we extend our treatment of sinusoidal steady-state analysis to lossy lines and also consider two special cases of pulses on lossy lines.Although the concepts and techniques discussed in this chapter are based on the analysis of transmission-line systems, many of these are also applicable to the analysis of other, analogous systems')
    speak('Finally, we extend our treatment of sinusoidal steady-state analysis to lossy lines and also consider two special cases of pulses on lossy lines. Although the concepts and techniques discussed in a a')
    # speak(sys.argv[1])
#    chinese_to_google('幹')
