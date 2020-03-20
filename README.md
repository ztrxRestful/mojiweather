# mojiweather
获取天气信息

初始化时，begin('省/直辖市'，'地级市/直辖市')  拼音  
例如：('shanghai','shanghai')  上海，上海  
例如：('shandong','jinan') 山东，济南  

等到的参数为（天气概要，风速，湿度，白天天气，夜晚天气，出行建议)  

weather_all, wind, humidity, morning_weather, night_weather, advise, pm25 = git_weather()  
