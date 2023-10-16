import matplotlib.pyplot as plt
from matplotlib import font_manager

kaiti_font = font_manager.FontProperties(family="KaiTi", size=20)
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn')
'''
采取了另一种常见的Matplotlib做法——调用函数subplots() （见❶）。这个函数可在一张图片中绘制一个或多
个图表。变量fig 表示整张图片。变量ax 表示图片中的各个图表，大多数情况下要使用它。
'''
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth = 3)  # 参数linewidth 决定了plot() 绘制的线条粗细

#设置图表标题并给坐标轴加上标签
ax.set_title("平方数", fontsize=24, fontproperties=kaiti_font)
ax.set_xlabel("值", fontsize=14, fontproperties=kaiti_font)
ax.set_ylabel("值的平方", fontsize=14, fontproperties=kaiti_font)
# 设置刻度标记的大小
ax.tick_params(axis='both', labelsize=14)

plt.show()