import sqlite3
try:
    import schedule
except ImportError:
    import subprocess
    subprocess.check_call(['pip', 'install', 'schedule'])
    exit()
from datetime import datetime

def save_to_database(date_time, temperature):
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS weather_data
              (date_time TEXT, temperature REAL)''')

def update_weather():
    dates = ["20 січня"] * 8
    times = ["03:00", "06:00", "09:00", "12:00", "15:00", "18:00", "21:00", "00:00"]
    temperatures = [-5, -5, -2, 1, 2, 1, -3, -6]

    current_date = datetime.now().strftime("%Y-%m-%d")

    for i in range(len(times)):
        date_time = f"{current_date} {times[i]}"
        temperature = temperatures[i]
        save_to_database(date_time, temperature)

update_weather()

schedule.every(30).minutes.do(update_weather())

try:
    while True:
        schedule.run_pending()
except KeyboardInterrupt:
    print("Програму зупинено.")
