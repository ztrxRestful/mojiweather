from urllib.request import urlopen
from bs4 import BeautifulSoup
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

        city = soup.select('ul>li')[3].string

        string = str(soup.select('html>head>meta')[2])

        list = string.split('"')

        msg = list[1].split('。')

        weather_all = msg[0].split('，')[0].split('：')[1]
        wind = msg[0].split('，')[2]
        humidity = msg[0].split('，')[1]

        morning_weather = msg[1]
        night_weather = msg[2]

        nlist = night_weather.split('，')

        night_weather = nlist[0][1:]+','+nlist[1]

        advise = ''
        for i in range(len(nlist)):
            if i > 1:
                advise += nlist[i]+'，'

        advise = advise[0:-1]+'。'
        # pm25 = soup.find_all('strong', class_='level_2')[0]
        # pm25 = str(pm25).split('\r')[1].strip()
        # pm_25 = pm25.split(' ')
        pm25 = soup.select('div>ul>li>a>span>img')[0]['alt']
        #print(pm25)
        pm_25 = pm25.split(' ')
        return city+'：'+weather_all,wind,humidity,morning_weather,night_weather,advise.replace('墨迹天气','阿德天气'),'PM2.5:'+pm_25[0]+'('+pm_25[1]+')'


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


