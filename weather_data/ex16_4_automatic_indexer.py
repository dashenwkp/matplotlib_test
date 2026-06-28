import csv
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt

path = Path(r'weather_data\sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()
reader = csv.reader(lines)
head_row = next(reader)

date_index = head_row.index('DATE')
high_index = head_row.index('TMAX')
low_index = head_row.index('TMIN')
name_index = head_row.index('NAME')

dates, highs, lows = [], [], []
name = ''

for row in reader:
    if not name:
        name = row[name_index]
    date = datetime.strptime(row[date_index], '%Y-%m-%d')
    try:
        high = int(row[high_index])
        low = int(row[low_index])
    except ValueError:
        print(f'Missing data for {date}')
    else:
        dates.append(date)
        highs.append(high)
        lows.append(low)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

ax.set_title(name, fontsize=24)
ax.set_xlabel('Date', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('The Most High and Low Temperature', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()