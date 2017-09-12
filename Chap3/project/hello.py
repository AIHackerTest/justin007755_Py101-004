from flask import Flask, render_template, request
from weatherWithAPI import queryFunc  # 复用Chap2的作业，直接调用其中的函数

weather_history = []
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/queryApp', methods=['POST', 'GET'])  # 同时支持POST和GET方法，因为第一个request是GET方法，取得home.html
def queryApp():
    if request.form['btn'] == '查询':  # 判断点击了哪个按钮
        #city_get = request.args.get('city')
        city_get = request.form['city']
        weather_get = queryFunc(city_get)
        weather_history.append(weather_get)
        return render_template('result.html', weather=weather_get)
    elif request.form['btn'] == '历史':
        return render_template('history.html', weather_his=weather_history)
    elif request.form['btn'] == '帮助':
        return render_template('help.html')


if __name__ == "__main__":
    app.run(debug=True)
