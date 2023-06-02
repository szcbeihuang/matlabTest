from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# 创建两个骰子
die1 = Die()
die2 = Die()

results = []

for roll_num in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)

frequencies = []
max_results = die1.num_sides + die2.num_sides
x_values = list(range(2, max_results + 1))
for x_value in x_values:
    frequency = results.count(x_value)
    frequencies.append(frequency)

# 可视化结果
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': '结果', 'dtick': 1}
y_axis_config = {'title': '结果的频率'}
my_layout = Layout(title='同时投掷两个骰子的结果频率',
                   xaxis=x_axis_config,
                   yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d62.html')


