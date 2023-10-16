from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline
import plotly.graph_objects as go
#
# die = Die()
# # 创建两个D6。
#
# results = []
# for roll_num in range(1000):
#     result = die.roll()
#     results.append(result)
# print(results)
#
# frequencies = []
# for value in range(1, die.num_sides + 1):
#     frequency = results.count(value)
#     frequencies.append( frequency )
# print(frequencies)
# print(sum(frequencies))
#
# # 对结果进行可视化。
# x_values = list(range(1, die.num_sides+1))
# data = [Bar(x=x_values, y=frequencies)]
# x_axis_config = {'title': '结果'}
# y_axis_config = {'title': '结果的频率'}
# my_layout = Layout(title='掷一个D6 1000次的结果', xaxis=x_axis_config, yaxis=y_axis_config)
# # offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')  # 生成HTML
# fig = go.Figure(data=data, layout=my_layout)
# fig.show()
# # offline.plot(fig, filename='d6.html') # 生成HTML

# -------------------------------------------------------------------------
#
# # 创建两个D6。
# die_1 = Die()
# die_2 = Die()
#
# results = []
# for roll_num in range(1000):
#     result = die_1.roll() + die_2.roll()
#     results.append(result)
# print(results)
#
# frequencies = []
# max_result = die_1.num_sides + die_2.num_sides
# for value in range(2, max_result+1):
#     frequency = results.count(value)
#     frequencies.append( frequency )
# print(frequencies)
# print(sum(frequencies))
#
# # 对结果进行可视化。
# x_values = list(range(2, max_result+1))
# data = [Bar(x=x_values, y=frequencies)]
# '''
# 在字典x_axis_config 中使用了dtick 键。这项设置指定了 轴显示的刻度间距。这里绘制的直方图包
# 含的条形更多，Plotly默认只显示某些刻度值，而设置'dtick': 1 让Plotly显示每个刻度值
# '''
# x_axis_config = {'title': '结果', 'dtick': 1}
# y_axis_config = {'title': '结果的频率'}
# my_layout = Layout(title='掷一个D6 1000次的结果', xaxis=x_axis_config, yaxis=y_axis_config)
# # offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')  # 生成HTML
# fig = go.Figure(data=data, layout=my_layout)
# fig.show()
# # offline.plot(fig, filename='d6_d6.html') # 生成HTML

# -------------------------------------------------------------------------

# 创建一个D6和一个D10。
die_1 = Die()
die_2 = Die(10)

results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
print(results)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append( frequency )
print(frequencies)
print(sum(frequencies))

# 对结果进行可视化。
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]
'''
在字典x_axis_config 中使用了dtick 键。这项设置指定了 轴显示的刻度间距。这里绘制的直方图包
含的条形更多，Plotly默认只显示某些刻度值，而设置'dtick': 1 让Plotly显示每个刻度值
'''
x_axis_config = {'title': '结果', 'dtick': 1}
y_axis_config = {'title': '结果的频率'}
my_layout = Layout(title='掷一个D6和一个D10 50000次的结果', xaxis=x_axis_config, yaxis=y_axis_config)
# offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')  # 生成HTML
fig = go.Figure(data=data, layout=my_layout)
fig.show()
# offline.plot(fig, filename='d6_d10.html') # 生成HTML