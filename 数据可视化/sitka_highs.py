import csv
import matplotlib.pyplot as plt
from matplotlib import font_manager
from datetime import datetime
#
# filename = 'data/sitka_weather_07-2018_simple.csv'
# kaiti_font = font_manager.FontProperties(family="KaiTi", size=20)
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#     print(header_row)
#     # for index, column_header in enumerate( header_row ):
#     #     print( index, column_header )
#     # 从文件中获取日期和最高温度。
#     dates, highs = [], []
#     for row in reader:
#         current_date = datetime.strptime( row[2], '%Y-%m-%d' )
#         high = int( row[5] )
#         dates.append( current_date )
#         highs.append( high )
#     print( dates )
#     print( highs )
#     plt.style.use( 'seaborn' )
#     fig, ax = plt.subplots()
#     ax.plot( dates, highs, c='red' )
#     # 设置图形的格式。
#     ax.set_title( "2018年7月每日最高温度", fontsize=24 , fontproperties=kaiti_font)
#     ax.set_xlabel( '', fontsize=16 )
#     fig.autofmt_xdate() # 用fig.autofmt_xdate() 来绘制倾斜的日期标签，以免其彼此重叠
#     ax.set_ylabel( "温度 (F)", fontsize=16, fontproperties=kaiti_font )
#     ax.tick_params( axis='both', which='major', labelsize=16 )
#     plt.show()

# ------------------------------------------------------------

filename = 'data/sitka_weather_2018_simple.csv'
kaiti_font = font_manager.FontProperties(family="KaiTi", size=20)
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    # for index, column_header in enumerate( header_row ):
    #     print( index, column_header )
    # 从文件中获取日期和最高温度。
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime( row[2], '%Y-%m-%d' )
        high = int( row[5] )
        dates.append( current_date )
        highs.append( high )
    print( dates )
    print( highs )
    plt.style.use( 'seaborn' )
    fig, ax = plt.subplots()
    ax.plot( dates, highs, c='red' )
    # 设置图形的格式。
    ax.set_title( "2018年每日最高温度", fontsize=24 , fontproperties=kaiti_font)
    ax.set_xlabel( '', fontsize=16 )
    fig.autofmt_xdate() # 用fig.autofmt_xdate() 来绘制倾斜的日期标签，以免其彼此重叠
    ax.set_ylabel( "温度 (F)", fontsize=16, fontproperties=kaiti_font )
    ax.tick_params( axis='both', which='major', labelsize=16 )
    plt.show()