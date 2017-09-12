# -*- coding: utf-8 -*-

def queryFun(cityInput):
    global hisWeather # 在本函数里更新所查过的城市记录
    dictWeather = {}

    with open('..\\resource\\weather_info.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            infoWeather = line.split(",")
            dictWeather[infoWeather[0]] = infoWeather[1].strip('\n')
    try:
        weather = dictWeather[cityInput]
    except KeyError:
        print("没有该城市，请核对或按h/help查询本程序的帮助")
    else:
        print(cityInput + '的天气状况为：' + weather)
        hisWeather.append(cityInput)
        hisWeather.append(weather)

def hisFun():
    for i in range(len(hisWeather)//2):
        print(hisWeather[i*2] + ' ' + hisWeather[i*2+1])


hisWeather = [] # 定义一个全局变量存放所有查询过的城市的天气情况

while True:

    cmdInput = input("请输入指令或您要查询的城市名： ")

    if cmdInput in ['help', 'h']:
        print('''
            输入城市名，查询该城市的天气；
            输入help/h，获取帮助文档；
            输入history，获取查询历史；
            输入quit/q，退出天气查询系统;
            ''')

    elif cmdInput in ['quit', 'exit', 'q', 'e']:
        hisFun()
        break

    elif cmdInput == 'history':
        print("您查过的天气情况如下：")
        hisFun()

    else:
        queryFun(cmdInput)
