# import requests
# import json
# key = '47e024bfb91adad6b67d1a0bf3aa8cef'
# city = input('Enter the city: ')
# parameters = {'c': city, 'appid' : key}
# url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric'
# res = requests.get(url)
# print(res)
# print(res.headers)
# print(res.text)
# print(res.status_code)
#
# json_result = res.text
# result = json.loads(json_result)
# print(json.dumps(result,indent = 4))
# with open('data.json','w') as file:
#     json.dump(json_result,file,indent = 4)
#
# print("Temperature",result['main']['temp']," C")
# print("Weather - ",result['weather'][0]['description'])
# print("Humidity",result['main']['humidity'],"%")
# print('Wind speed',result['wind']['speed'])
# print("Pressure",result['main']['pressure'])
# print("Minimal temperature",result['main']['temp_min'],"C")
# print("Maximal temperature",result['main']['temp_max'],"C")
#
# ##Cxrilshi mocemuli iqneba Kutaisi batumisa da tbilisis amindi da temperatura
# import sqlite3
# conn = sqlite3.connect("my_db.sqlite")
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS weather
#                (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                city VARCHAR(10),
#                theweather VARCHAR(20),
#                temperature FLOAT); ''')
#
# weather_list = [('Tbilisi','clear sky',17.84),
#                 ('Kutaisi','clear sky',18.43),
#                 ('Batumi','few clous', 13.99)
#                 ]
# cursor.executemany("INSERT INTO weather(city,theweather,temperature) VALUES(?,?,?)",weather_list)
#
# conn.commit()
# conn.close()






