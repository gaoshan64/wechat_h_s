# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import requests
import json

print 'get_weather'
def get_weather():
    weather_su=requests.get(url='https://api.seniverse.com/v3/life/suggestion.json?key=cnlsyrhgx9dczlzi&location=shenyang&language=zh-Hans')
    weather_re=requests.get("https://api.seniverse.com/v3/weather/daily.json?key=cnlsyrhgx9dczlzi&location=shenyang&language=zh-Hans&unit=c&start=0&days=1")
#print weather_re.text
    print weather_su.text
    weather_su=eval(weather_su.text)
    weather_re=eval(weather_re.text)

    weather_su=weather_su['results'][0]['suggestion']
    weather_re=weather_re['results'][0]['daily'][0]
    print type(weather_re),type(weather_su)

    f_date=weather_re['date']
    f_day =weather_re['text_day']
    f_night =weather_re['text_night']
    f_t_h = weather_re['high']
    f_t_l =weather_re['low']
    f_w_d = weather_re['wind_direction']
    f_w_sc =weather_re['wind_scale']

    f_car_washing = weather_su['car_washing']['brief']
    f_dressing =weather_su['dressing']['brief']
    f_flu =weather_su['flu']['brief']
    f_sport=weather_su['sport']['brief']
    f_travel =weather_su['travel']['brief']
    f_uv =weather_su['uv']['brief']

    print f_date,f_day,f_night,f_t_h,f_t_l,f_w_d,f_w_sc,f_car_washing,f_dressing,f_flu,f_sport,f_travel,f_uv
    final_report = '天气预报\n'+f_date+'\n'+'白天天气:'+f_day+'\n'+'夜间天气:'+f_night+'\n'+'最高气温:'+f_t_h+'\n'+'最低气温:'+f_t_l+'\n'\
    +'风力风向:'+f_w_d+' '+f_w_sc+'级\n'+'穿衣指数：'+f_dressing+'\n'+'流感：'+f_flu+'\n'+'紫外线:'+f_uv+'\n'+'运动：'+f_sport+'\n'\
    +'洗车:'+f_car_washing+'\n'+'运动:'+f_sport+'\n'+'旅行:'+f_travel
    return final_report
final_report = get_weather()
print final_report
