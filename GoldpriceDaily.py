import requests
import time
import json
import datetime

# Format data as an HTML table
now = datetime.date.today()
def getgoldPrice():
    try:
        response=requests.get("https://service.upstox.com/scrip-details-fundamentals/v1/gold-price/major-cities")
        data=response.text
        return data
    except Exception as e:
        print(e)

def send_to_telegram(data):

    apiToken = '6710141652:AAFRAWQb1r_9c0ZYl9NZ9mGCZ_EUlDkZAcU'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'
    data=json.loads(data)
    html_table = "<b>CityName</b> | <b>Price 24k</b> | <b>Price 22k - {date}</b>\n".format(date=now)
    html_table += "--------------|----------------|----------------\n"
    for city_data in data["data"]["majorCities"]:
        html_table += f"{city_data['cityName']} | {city_data['price24k']} | {city_data['price22k']}\n"

    params = {
    "chat_id": "@goldpricein",
    "text": html_table,
    "parse_mode": "HTML",
}
    try:
        response = requests.post(apiURL, params=params)
        print(response.text)
    except Exception as e:
        print(e)
# time.sleep(5)
send_to_telegram(getgoldPrice())
