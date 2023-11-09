import requests
import setting

# LINE Notify APIのトークン
TOKEN = setting.TOKEN
# 天気情報を取得する都市名とAPIキー
city_name = "Chikuma"
API_KEY = setting.AP
api = "http://api.openweathermap.org/data/2.5/weather?units=metric&q={city}&APPID={key}"

# 天気情報を取得するAPIにアクセスしてデータを取得
url = api.format(city=city_name, key=API_KEY)
response = requests.get(url)
data = response.json()

# 天気情報をLINE Notify APIを利用してメッセージを送信
temp = data['main']['temp']
message = f"現在の{city_name}の気温は{temp}℃です。\n体感温度は{data['main']['feels_like']}℃です。"
hot = 30
cold = 5
if temp > hot:
    message += "\n今日はとても暑いです。熱中症に気をつけましょう！"
elif temp < cold:
    message += "\n今日はとても寒いです。防寒対策をしましょう！"

humidity = data['main']['humidity']
pressure = data['main']['pressure']
try:
    rain = data['rain']['1h']
    message += f"\n降水確率は{rain}%です。"
except KeyError:
    message += "\n降水確率は不明です。"

message += f"\n湿度は{humidity}%で、気圧は{pressure} hPaです。"
low_pressure = 1000
if pressure <= low_pressure:
    message += "\n頭痛に注意してください。"

headers = {"Authorization": f"Bearer {TOKEN}"}
payload = {"message": message}
requests.post("https://notify-api.line.me/api/notify", headers=headers, data=payload)
