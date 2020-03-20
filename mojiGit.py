from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys
sys.path.append(r'C:\Users\Administrator\PycharmProjects\weixin')
import wechat

class begin():
    def __init__(self,shen,city):
        self.shen = shen
        self.city = city

    def git_weather(self):
        url = "https://tianqi.moji.com/weather/china/"+self.shen+"/"+self.city
        html = urlopen(url).read().decode('utf-8')
        #print(html)
        soup = BeautifulSoup(html,'html.parser')
        #print(res.content)
        #print(res.headers)
        #print(soup.select('html>head>meta')[2])
        #print(soup.select('ul>li')[3].string)
        city = soup.select('ul>li')[3].string
        #print(city)
        string = str(soup.select('html>head>meta')[2])
        #print(type(string))
        list = string.split('"')
        #print(list[1])
        msg = list[1].split('。')
        #print(msg)
        #print(msg[0].split('，')[0].split('：')[1])
        weather_all = msg[0].split('，')[0].split('：')[1]
        wind = msg[0].split('，')[2]
        humidity = msg[0].split('，')[1]

        morning_weather = msg[1]
        night_weather = msg[2]
        #print()
        nlist = night_weather.split('，')
        #print(nlist[0][1:]+'，'+nlist[1])
        night_weather = nlist[0][1:]+','+nlist[1]
        # print(weather_all)
        # print(wind)
        # print(humidity)
        # print(morning_weather)
        # print(night_weather)
        advise = ''
        for i in range(len(nlist)):
            if i > 1:
                advise += nlist[i]+'，'

        advise = advise[0:-1]+'。'
        pm25 = soup.find_all('strong', class_='level_2')[0]
        pm25 = str(pm25).split('\r')[1].strip()
        pm_25 = pm25.split(' ')
        #print(pm25.split(' '))
        #print(pm_25[0]+'('+pm_25[1]+')')
        return city+'：'+weather_all,wind,humidity,morning_weather,night_weather,advise.replace('墨迹天气','阿德天气'),'PM2.5:'+pm_25[0]+'('+pm_25[1]+')'
#putuo-district

if __name__ == '__main__':
    moji = begin('shanghai','shanghai')
    weather_all, wind, humidity, morning_weather, night_weather, advise, pm25 = moji.git_weather()
    print(weather_all)
    print(wind)
    print(humidity)
    print(morning_weather)
    print(night_weather)
    print(pm25)
    print(advise)

    # weixin = wechat.begin('C:\Program Files (x86)\Tencent\WeChat')
    # weixin.open_wechat()
    # weixin.send_msg_obj('Hammer')
    #
    # weixin.send_msg(weather_all)
    # weixin.huang_hang()
    #
    # weixin.send_msg(wind)
    # weixin.huang_hang()
    #
    # weixin.send_msg(humidity)
    # weixin.huang_hang()
    #
    # weixin.send_msg(morning_weather)
    # weixin.huang_hang()
    #
    # weixin.send_msg(night_weather)
    # weixin.huang_hang()
    #
    # weixin.send_msg(pm25)
    # weixin.huang_hang()
    #
    # weixin.send_msg(advise)
    # weixin.huang_hang()
    #
    # weixin.send()
