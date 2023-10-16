import matplotlib.pyplot as plt
from matplotlib import font_manager


kaiti_font = font_manager.FontProperties(family="KaiTi", size=20)
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]
plt.style.use('seaborn')
fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, s=10, c='red')  # 调用scatter() 并使用参数s 设置绘制图形时使用的点的尺寸  .c设置颜色
# ax.scatter(x_values, y_values, s=10, c=(0, 0.8, 0))  # 调用scatter() 并使用参数s 设置绘制图形时使用的点的尺寸  .c设置颜色
ax.scatter(x_values, y_values, s=10, c=y_values, cmap=plt.cm.Blues)  # cmap 颜色映射
# 设置图表标题并给坐标轴加上标签。
ax.set_title("平方数", fontsize=24, fontproperties=kaiti_font)
ax.set_xlabel("值", fontsize=14, fontproperties=kaiti_font)
ax.set_ylabel("值的平方", fontsize=14, fontproperties=kaiti_font)
# 设置刻度标记的大小。
ax.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标轴的取值范围。
ax.axis([0, 1100, 0, 1100000])
plt.show()
# 自动保存图表
# plt.savefig('squares_plot.png', bbox_inches='tight')
