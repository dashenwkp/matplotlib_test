import matplotlib.pyplot as plt

input_values = range(1, 5001)
cubes = [x ** 3 for x in input_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(input_values, cubes, c=cubes, cmap=plt.cm.Blues, s=10)

ax.set_title('Cube Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Cube of Value', fontsize=14)

ax.tick_params(labelsize=14)

plt.show()