import csv
import matplotlib.pyplot as plt
from matplotlib import font_manager
from datetime import datetime


filename = 'data/death_valley_2018_simple.csv'
kaiti_font = font_manager.FontProperties(family="KaiTi", size=20)
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    # for index, column_header in enumerate( header_row ):
    #     print( index, column_header )
    # 从文件中获取日期、最高温度和最低温度。
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime( row[2], '%Y-%m-%d' )
        try:
            high = int( row[4] )
            low = int( row[5] )
        except ValueError:
            print( f"Missing data for {current_date}" )
        else:
            dates.append( current_date )
            highs.append( high )
            lows.append( low )
    print( dates )
    print( highs )
    print( lows )
    plt.style.use( 'seaborn' )
    fig, ax = plt.subplots()
    ax.plot( dates, highs, c='red', alpha=0.5 ) # 实参alpha 指定颜色的透明度。alpha 值为0表示完全透明，为1（默认设置）表示完全不透明
    ax.plot( dates, lows, c='blue', alpha=0.5 )
    '''
    fill_between() 传递一个 值系列（列表dates ），以及两个 值系列（highs 和lows ）。
    实参facecolor指定填充区域的颜色，还将alpha 设置成了较小的值0.1，让填充区域将两个数据系列连接起来的同时不分散观察者的注意力
    '''
    ax.fill_between( dates, highs, lows, facecolor='blue', alpha=0.1 )
    # 设置图形的格式。
    ax.set_title( "2018年每日最高温度和最低温度\n美国加利福尼亚州死亡谷", fontsize=20 , fontproperties=kaiti_font)
    ax.set_xlabel( '', fontsize=16 )
    fig.autofmt_xdate() # 用fig.autofmt_xdate() 来绘制倾斜的日期标签，以免其彼此重叠
    ax.set_ylabel( "温度 (F)", fontsize=16, fontproperties=kaiti_font )
    ax.tick_params( axis='both', which='major', labelsize=16 )
    plt.show()