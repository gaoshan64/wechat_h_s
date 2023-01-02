# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : message_sender.py
# Time       ：2022/9/3 19:49
# Author     ：Gao Shan
# Description：
"""

from wechat_sender import Sender

def send_message_test():
    Sender(receivers=u"gaoshan'secretary").send('test')


if __name__ == '__main__':
    send_message_test()