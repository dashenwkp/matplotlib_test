from die import Die

import plotly.express as px

die_1 = Die()
die_2 = Die()
results = []

# 掷几次骰子并将结果放在一个列表中
for roll_num in range(10000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
poss_value = range(1, max_result + 1)
for value in poss_value:
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
title = 'Results of Rolling Dices'
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_value, y=frequencies, title=title, labels=labels)

# 进一步定制图形
fig.update_layout(xaxis_dtick=1)

fig.show()