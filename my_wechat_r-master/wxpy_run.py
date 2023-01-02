# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from wxpy import *
from wechat_sender import *
import get_weather
robot=Bot(cache_path=True,console_qr=True)
mis = ensure_one(robot.groups().search(u'MIS'))
changyuan_1 =ensure_one(robot.groups().search(u'畅园1号楼业主群'))
changyuan_2=ensure_one(robot.groups().search(u'畅园全体业主2群'))
daoban = ensure_one(robot.groups().search(u"宅家经验分享交流"))
testtest = ensure_one(robot.groups().search(u'试验用群'))


gaoya= ensure_one(robot.friends().search("gaoshan'secretary"))
baba = ensure_one(robot.friends().search(u"高起"))
mama = ensure_one(robot.friends().search(u"庞亚男"))
chouchou = ensure_one(robot.friends().search(u'丑丑'))
boss = ensure_one(mis.search(u'张晓'))
jiangjiang = ensure_one(robot.friends().search(u'优先回复群消息'))

print mis
print chouchou
print baba
print mama
print daoban
print testtest
print changyuan_1
print changyuan_2
print boss


@robot.register()
def print_messages(msg):
    print(msg)

@robot.register(mis)
def forward_boss_message(msg):
    if msg.member == boss:
        msg.forward(robot.file_helper, prefix='老板发言')
        msg.forward(gaoya,prefix='老板发言')

@robot.register(gaoya)
def replay_weather(msg):
    print msg.text
    if u'天气' in msg.text:
        
        msg.reply(get_weather.get_weather())
    if u'博客ip' in msg.text:
        with open('./cip.txt','r') as f:
            cip = f.read()
            cipurl='https://%s:8443/wordpress/'%cip
        msg.reply(cipurl)
    if u'博客地址' in msg.text:
        msg.reply('https://www.gaoshan.ink:8443/wordpress')
    if u'窗外' in msg.text:
        msg.reply_image('./capture.jpg')

'''
@robot.register(testtest)
def sent_image(msg):
    print msg.text
    if  u'人多么' in msg.text:
        msg.reply_image('./test.jpg')
'''
#embed()
listen(robot,receivers=[gaoya,testtest,daoban,chouchou,baba,mama])

