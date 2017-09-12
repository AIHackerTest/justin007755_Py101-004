# -*- coding: utf-8 -*-
import requests, json

hisWeather = []    # 定义一个全局变量存放所有查询过的城市的天气情况
degreeFlag = 1  # 表示摄氏度,如果degreeFlag=0则表示华氏度

def fetchWeather(location, UNIT):
    result = requests.get(
        'https://api.seniverse.com/v3/weather/daily.json',
        params={
        'key': '5dwuvzffb3vliljg',
        'location': location,
        'language': 'zh-Hans',
        'unit': UNIT
    },
    timeout=30)
    return result.text

def queryFunc(cityInput):
    global hisWeather   # 在本函数里更新所查过的城市记录
    dictWeather = {}
    unitShow = '摄氏度'

    try:
        if degreeFlag == 1:
            rtnData = fetchWeather(cityInput, 'c')
            unitShow = '摄氏度'
        else:
            rtnData = fetchWeather(cityInput, 'f')
            unitShow = '华氏度'
        text = json.loads(rtnData)
        todayData = text['results'][0]['daily'][0]
        dateToday, weather, tempHigh, tempLow = todayData['date'], todayData['text_day'], todayData['high'], todayData['low']
        updatedTime = text['results'][0]['last_update'][:-6].replace('T', ' ')
    except KeyError:
        print("没有该城市，请核对或按h/help查询本程序的帮助")
    else:
        print(dateToday + '\n' + cityInput + '的天气为: ' + weather + ',最高温度为' + tempHigh +
              unitShow + ',最低温度为' + tempLow + unitShow +'\n' + '更新时间：' + updatedTime)
        hisWeather.append(cityInput)
        hisWeather.append(weather)

def hisFunc():
    for i in range(len(hisWeather) // 2):
        print(hisWeather[i * 2] + ' ' + hisWeather[i * 2 + 1])


while True:

    cmdInput = input("\n请输入指令或您要查询的城市名： ")

    if cmdInput in ['help', 'h']:
        print('''
            输入城市名，查询该城市的天气；
            输入help/h，获取帮助文档；
            输入history，获取查询历史；
            输入quit/q，退出天气查询系统;
            输入f为华氏度,c为摄氏度,系统缺省为c为摄氏度;
            ''')

    elif cmdInput in ['quit', 'exit', 'q', 'e']:
        hisFunc()
        break

    elif cmdInput == 'history':
        print("您查过的天气情况如下：")
        hisFunc()

    elif cmdInput == 'f':
        degreeFlag = 0
        print("转换为华氏度")

    elif cmdInput == 'c':
        degreeFlag = 1
        print("转换为摄氏度度")

    else:
        queryFunc(cmdInput)
