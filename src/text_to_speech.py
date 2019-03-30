from googletrans.gtoken import TokenAcquirer
import vlc
import sys
from time import sleep
from urllib.parse import quote


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
    i = vlc.Instance()
    p = i.media_player_new()
    url = 'http://translate.google.com.tw/translate_tts?ie=UTF-8&q={string}&tl={lang}&total=1&idx=0&textlen={len}&tk={token}&client=webapp&prev=input'.format(string=quote(string), lang=language(
        string), len=get_len(string), token=get_token(string))
    # url = 'https://translate.google.com.tw/translate_tts?ie=UTF-8&q=%E8%B6%95%E7%BE%9A%E7%BE%8A&tl=zh-CN&total=1&idx=0&textlen=3&tk=353679.254520&client=t&prev=input&ttsspeed=0.24'
    print('The url is:', url)
    p.set_mrl(url)
    p.play()
    sleep(1.5)
    duration = p.get_length() // 1000
    sleep(duration + 1)


if __name__ == '__main__':
    speak(sys.argv[1])
#    chinese_to_google('幹')
