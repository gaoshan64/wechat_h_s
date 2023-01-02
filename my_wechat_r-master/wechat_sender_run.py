# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from wechat_sender import Sender
import get_weather
import get_english


def send_hello():
    Sender(receivers=u"gaoshan\'secretary").send(u'早上好！')



def send_price(url='https://www.michelin.com/eng/finance/share-information/share-price-history'):

    Sender(receivers=u"gaoshan'secretary").send(u'今日米其林股今日米其林股价信息'+url)

def send_ip():
    with open('./cip.txt', 'r') as f:
        cip = f.read()
        cipurl = 'https://%s:8443/wordpress/' % cip
    Sender(receivers=u"gaoshan'secretary").send(cipurl)


def send_weather(weather):
    Sender(receivers=u"gaoshan'secretary").send(weather)

def send_english(english):
    Sender(receivers=u"gaoshan'secretary").send(english)



send_hello()
#send_price()
send_ip()
send_weather(get_weather.get_weather())
send_english(get_english.english_send)
