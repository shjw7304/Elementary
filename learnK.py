# -*- coding:utf-8 -*-
import matplotlib as mpl
import tushare as ts
import matplotlib.pyplot as plt
import mpl_finance as mpf
from matplotlib.pylab import date2num
import datetime
import matplotlib.dates as mdates
import numpy as np

wdyx = ts.get_k_data('000001','2017-01-01')
#wdyx.info()

print(wdyx[:3])

def date_to_num(dates):
    num_time = []
    for date in dates:
        date_time = datetime.datetime.strptime(date,'%Y-%m-%d')
        #print("date_time",date_time)
        num_date = date2num(date_time)
        #print("num_date", num_date)
        num_time.append(num_date)
    return num_time
# dataframe转换为二维数组


mat_wdyx = wdyx.values
#print(mat_wdyx[:,0])
num_time1 = mat_wdyx[:,0]
num_time = date_to_num(mat_wdyx[:,0])


mat_wdyx[:,0] = num_time
#         日期,   开盘,     收盘,    最高,      最低,   成交量,    代码
print(mat_wdyx[:3])

fig = plt.figure()
#ax = plt.subplot2grid((4, 4), (0, 0), rowspan=3, colspan=4)
ax = plt.subplot(2,1,1)

#fig, ax = plt.subplots(figsize=(15,5))
#fig.subplots_adjust(bottom=0.5)

mpf.candlestick_ochl(ax, mat_wdyx, width=0.6, colorup='g', colordown='r', alpha=0.1)
'''
opens = np.arange(-10,10,0.1)
closes = np.arange(-10,10,0.1)
highs = np.arange(-10,10,0.1)
lows = np.arange(-10,10,0.1)

mpf.candlestick2_ochl(ax, opens, closes, highs, lows, width=4, colorup='k', colordown='r', alpha=0.75)
'''
plt.grid(True)
# 设置日期刻度旋转的角度
plt.xticks(rotation=30)
plt.title('wanda yuanxian 17')
plt.xlabel('Date')
plt.ylabel('Price')

plt.xticks([])

###candlestick_ochl()函数的参数
# ax 绘图Axes的实例
# mat_wdyx 价格历史数据
# width    图像中红绿矩形的宽度,代表天数
# colorup  收盘价格大于开盘价格时的颜色
# colordown   低于开盘价格时矩形的颜色
# alpha      矩形的颜色的透明度
#ax2 = plt.subplot2grid((4, 4), (3, 0), colspan=4)
ax2 = plt.subplot(2,1,2)

ax2.bar(num_time1,mat_wdyx[:,5])
ax2.set_ylabel("Volume")
ax2.xaxis.set_major_locator(mdates.MonthLocator())
ax2.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
for label in ax2.xaxis.get_ticklabels():
  label.set_rotation(45)
plt.grid(True)



plt.show()