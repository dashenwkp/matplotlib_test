from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path(r'weather_data\sitka_weather_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# 提取日期和降水量
dates, prcps = [], []
for row in reader:
    date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        prcp = float(row[5])
    except ValueError:
        print(f'Missing the data of {date}')
    else:
        dates.append(date)
        prcps.append(prcp)

# 绘图
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, prcps, color='blue')

# 设置绘图的格式
ax.set_title('The PRCP of the Sitka', fontsize=24)
ax.set_xlabel('Date', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('PRCP', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()