import requests
city = 'sidi bel abbes'
lang = 'ar'
days = '2'
# go and get api_key from
#https: // www.weatherapi.com
api_key = '77913e80ebc54ec3aa0104817210110'
the_data = requests.get(f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days={days}&aqi=no&alerts=no&lang={lang}').json()


def display_data():
    return f"city name: {the_data['location']['name']}\n" \
           "" \
           f"last update: {the_data['current']['last_updated']}\n" \
           f"" \
           f"Temp: {the_data['current']['temp_c']}C°\n" \
           f"" \
           f"description: {the_data['current']['condition']['text']}\n" \
           f"" \
           f"data: {the_data['forecast']['forecastday'][1]['date']}\n" \
           f"" \
           f"Tomorrow description: {the_data['forecast']['forecastday'][1]['day']['condition']['text']}\n" \
           f"" \
           f"" \
           f"" \
           f"max Temp: {the_data['forecast']['forecastday'][1]['day']['maxtemp_c']}C°\n" \
           f"" \
           f"min Temp: {the_data['forecast']['forecastday'][1]['day']['mintemp_c']}C°\n" \
           f"" \
           f"avg Temp: {the_data['forecast']['forecastday'][1]['day']['avgtemp_c']}C°\n" \
           f"" \
           f"#######################################################################################\n\n\n" \
           f"" \
           f"Take Care form 'Yasser'\n"

#     print(the_data)
    # print(f"city name: {the_data['location']['name']}")
    # print(f"last update: {the_data['current']['last_updated']}")
    # print(f"Temp: {the_data['current']['temp_c']}C°")
    # print(f"description: {the_data['current']['condition']['text']}")

    # print("##########################\ntomorrow: ")

    # print(f"data: {the_data['forecast']['forecastday'][1]['date']}")
    # print(f"Tomorrow description: {the_data['forecast']['forecastday'][1]['day']['condition']['text']}")

    

    # print(f"max Temp: {the_data['forecast']['forecastday'][1]['day']['maxtemp_c']}C°")
    # print(f"min Temp: {the_data['forecast']['forecastday'][1]['day']['mintemp_c']}C°")
    # print(f"avg Temp: {the_data['forecast']['forecastday'][1]['day']['avgtemp_c']}C°")

#display_data()