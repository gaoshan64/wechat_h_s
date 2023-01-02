# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : test1.py
# Time       ：2022/9/3 1:23
# Author     ：Gao Shan
# Description：
"""

from wxpy import *
from wechat_sender import *

robot = Bot(cache_path=True, console_qr=True)
helper = ensure_one(robot.friends().search("gaoshan'secretary"))
gaoshan = ensure_one(robot.friends().search("高山"))
school_group = ensure_one(robot.groups().search(u'盛京小学 一年三班'))
chouchou = ensure_one(robot.friends().search(u'丑丑'))
laolao = ensure_one(robot.friends().search(u'雅雅姥姥'))
teacher_li = ensure_one(school_group.search(u'李悦老师'))
testgroup = ensure_one((robot.groups().search(u'试验用群')))

gaoshan_school_group=ensure_one(school_group.search(u'高巽爸爸'))
chouchou_school_group=ensure_one(school_group.search(u'高巽妈妈'))

print('''

家校群        {}
高雅姥姥       {}
班主任李老师    {}
小秘书         {}
高山          {}
丑丑          {}
试验群         {}
----------------------
高山——家长群    {}
丑丑——家长群    {}
'''.format(school_group, laolao, teacher_li, helper, gaoshan, chouchou, testgroup,
           gaoshan_school_group,chouchou_school_group))

gaoshan.send('send_message_test')


forward_suffix='%此信息由高小雅自动转发'

@robot.register(school_group)
def forward_teacher_message(msg):
    print(msg)
    if msg.member == teacher_li:
        #print(msg)
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!/n')
        msg.forward(robot.file_helper, prefix='雅雅班主任(班级群)：', suffix =forward_suffix)
        msg.forward(helper, prefix='雅雅班主任(班级群)：', suffix =forward_suffix)
        msg.forward(chouchou, prefix='雅雅班主任(班级群)：', suffix =forward_suffix)
        msg.forward(laolao, prefix='雅雅班主任(班级群)：', suffix =forward_suffix)

    if msg.member == gaoshan_school_group:
        #print(msg)
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!/n')
        msg.forward(robot.file_helper, prefix='高山(班级群)：', suffix=forward_suffix)
        msg.forward(helper, prefix='高山(班级群)：', suffix =forward_suffix)
        msg.forward(chouchou, prefix='高山(班级群)：', suffix =forward_suffix)
        msg.forward(laolao, prefix='高山(班级群)：', suffix =forward_suffix)

    if msg.member == chouchou_school_group:
        #print(msg)
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!/n')
        msg.forward(helper, prefix='丑丑(班级群)：', suffix =forward_suffix)
        msg.forward(robot.file_helper, prefix='丑丑(班级群)：', suffix=forward_suffix)
        msg.forward(chouchou, prefix='丑丑(班级群)：', suffix =forward_suffix)
        msg.forward(laolao, prefix='丑丑(班级群)：', suffix =forward_suffix)


@robot.register(testgroup)
def forward_test(msg):
    if msg.member == helper:
        
        print(msg)
        msg.forward(gaoshan, prefix='测试助手(试验群)：',suffix =forward_suffix)
        #gaoshan.send(msg)


embed()
