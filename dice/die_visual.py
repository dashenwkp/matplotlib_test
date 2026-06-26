from die import Die

import plotly.express as px

die = Die()
results = []

# 掷几次骰子并将结果放在一个列表中
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = []
poss_value = range(1, die.num_sides + 1)
for value in poss_value:
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
title = 'Results of Rolling One D6 1000 Times'
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_value, y=frequencies, title=title, labels=labels)
fig.show()