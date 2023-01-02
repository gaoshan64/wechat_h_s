#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/9 21:24
# @Author  : Gaoshan
# @Site    : 
# @File    : capture.py
# @Software: PyCharm
import sys
import os

reload(sys)
sys.setdefaultencoding('utf-8')

def capture():
    os.system('del -F test.jpg')


if __name__ == '__main__':
    capture()