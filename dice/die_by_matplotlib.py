import matplotlib.pyplot as plt

from die import Die

die1 = Die()
die2 = Die()

# 掷几次骰子并将结果放在一个列表中
results = [die1.roll() + die2.roll() for _ in range(10000)]

# 分析结果，获得频数
poss_value = range(1, die1.num_sides + die2.num_sides + 1)
frequencies = [results.count(value) for value in poss_value]

# 对结果进行可视化
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.bar(poss_value, frequencies)

ax.set_title('Rolling Dice', fontsize=24)
ax.set_xlabel('Possibile Results', fontsize=14)
ax.set_ylabel('Frequencies', fontsize=14)

plt.show()