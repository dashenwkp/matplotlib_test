from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path(r'weather_data\sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# 提取日期，最高温度和最低温度
highs, dates, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    low = int(row[5])
    highs.append(high)
    dates.append(current_date)
    lows.append(low)

# 根据最高和最低温度绘图
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置绘图的格式
ax.set_title('Daily High and Low Temperatures, 2021', fontsize=24)
ax.set_xlabel('Date', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.tick_params(labelsize=16)
plt.yticks([0, 25, 50, 75, 100], ['0', '25', '50', '75', '100'])
plt.show()