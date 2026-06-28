import csv
from pathlib import Path
from datetime import datetime

import matplotlib.pyplot as plt

def get_weather_date(path, dates, highs, lows, date_index, high_index, low_index):
    '''获取日期，最高温和最低温度的数据'''
    lines = path.read_text().splitlines()
    reader = csv.reader(lines)
    head_row = next(reader)

    for row in reader:
        date = datetime.strptime(row[date_index], '%Y-%m-%d')
        try:
            high = int(row[high_index])
            low = int(row[low_index])
        except ValueError:
            print(f'Missing data of {date}')
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)

path = Path(r'weather_data\sitka_weather_2021_simple.csv')
dates, highs, lows = [], [], []
get_weather_date(path, dates, highs, lows, 2, 4, 5)
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

path = Path(r'weather_data\death_valley_2021_simple.csv')
dates, highs, lows = [], [], []
get_weather_date(path, dates, highs, lows, 2, 3, 4)
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

title = '' \
'Daily high and low temperatures - 2021\nSitka, AK and Death Valley, CA'
ax.set_title(title, fontsize=24)
ax.set_xlabel('Date', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.tick_params(labelsize=16)
ax.set_ylim(10, 140)

plt.show()