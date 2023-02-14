import requests
import json


def weather(city):
    url = "https://yahoo-weather5.p.rapidapi.com/weather"

    querystring = {"location": f"{city}", "format": "json", "u": "f"}

    headers = {
        "X-RapidAPI-Key": "98b5e30546msh0bb833bdfd28e74p1ffa57jsncf5206925676",
        "X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    if response.status_code == 200:
        data = json.loads(response.text)
        harorat = (data['current_observation']['condition']['temperature'] - 32) * 5 / 9
        result = f"🌆 Shahar : {data['location']['city']}\n" \
                 f"🌄 Quyosh chiqish vaqti : {data['current_observation']['astronomy']['sunrise']}\n" \
                 f"🌇 Quyosh botish vaqti : {data['current_observation']['astronomy']['sunset']}\n" \
                 f"🌡 Harorat : {'{:.2f}'.format(harorat)}"
        return result
    else:
        return 'Error'
