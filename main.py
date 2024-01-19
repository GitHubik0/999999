import sqlite3
import requests
from bs4 import BeautifulSoup
import datetime

# Створення бази даних
conn = sqlite3.connect('weather_1.sl3')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS weather_data
              (date_time TEXT, temperature REAL)''')

# Отримання інформації про температуру з веб-сайту
url = 'https://www.accuweather.com/uk/ua/lutsk/326220/weather-forecast/326220'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Отримання поточної дати та часу
current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Перевірка наявності тега span з класом temperature
temperature_span = soup.find('span', {'class': 'temperature'})
if temperature_span:
    temperature = float(temperature_span.text.strip())
    print(f'Temperature: {temperature}')

    # Внесення даних в базу даних
    c.execute("INSERT INTO weather_data (date_time, temperature) VALUES (?, ?)", (current_datetime, temperature))
    conn.commit()
else:
    print('Unable to find temperature information on the page')

# Закриття з'єднання з базою даних
conn.close()
