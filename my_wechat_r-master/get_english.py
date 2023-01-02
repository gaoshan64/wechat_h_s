# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import requests

import urllib2
import json
def get_iciba_everyday():
    url = 'http://open.iciba.com/dsapi/'
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    json_data = response.read()
    data = json.loads(json_data)
    return data

data = get_iciba_everyday()

english= data['content']
chinese = data['note']
english_send = u'每日一句'+'\n'+u'英文:'+english+'\n'+u'翻译：'+chinese




