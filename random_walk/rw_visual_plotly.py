import plotly.express as px

from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_work()

title = 'Random Work'
labels = {'x': 'x', 'y': 'y'}

fig = px.scatter(x=rw.x_values, y=rw.y_values, title=title, labels=labels)

fig.show()