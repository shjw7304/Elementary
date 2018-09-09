# -*- coding:utf-8 -*-
import matplotlib as mpl
import tushare as ts
import matplotlib.pyplot as plt
import mpl_finance as mpf
from matplotlib.pylab import date2num
import datetime


wdyx = ts.get_k_data('002739','2017-01-01')
wdyx.info()

print(wdyx[:3])

def date_to_num(dates):
    num_time = []
    for date in dates:
        date_time = datetime.datetime.strptime(date,'%Y-%m-%d')
        num_date = date2num(date_time)
        num_time.append(num_date)
    return num_time
# dataframe转换为二维数组
mat_wdyx = wdyx.as_matrix()
num_time = date_to_num(mat_wdyx[:,0])
mat_wdyx[:,0] = num_time
#         日期,   开盘,     收盘,    最高,      最低,   成交量,    代码
print(mat_wdyx[:3])

fig, ax = plt.subplots(figsize=(15,5))
#fig.subplots_adjust(bottom=0.5)

mpf.candlestick_ochl(ax, mat_wdyx, width=0.6, colorup='g', colordown='r', alpha=1.0)
plt.grid(True)
# 设置日期刻度旋转的角度
plt.xticks(rotation=30)
plt.title('wanda yuanxian 17')
plt.xlabel('Date')
plt.ylabel('Price')
# x轴的刻度为日期
ax.xaxis_date ()
###candlestick_ochl()函数的参数
# ax 绘图Axes的实例
# mat_wdyx 价格历史数据
# width    图像中红绿矩形的宽度,代表天数
# colorup  收盘价格大于开盘价格时的颜色
# colordown   低于开盘价格时矩形的颜色
# alpha      矩形的颜色的透明度

plt.show()