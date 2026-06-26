from die import Die

import plotly.express as px

die_1 = Die()
die_2 = Die()
results = [die_1.roll() + die_2.roll() for _ in range(50000)]

# 分析结果
max_result = die_1.num_sides + die_2.num_sides
poss_value = range(2, max_result + 1)
frequencies = [results.count(value) for value in poss_value]

# 对结果进行可视化
title = 'Results of Rolling a D6 and a D8 50000 Times'
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_value, y=frequencies, title=title, labels=labels)

# 进一步定制图形
fig.update_layout(xaxis_dtick=1)

fig.show()