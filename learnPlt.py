import  matplotlib.pyplot as plt
import  numpy as np
#import matplotlib.finance as mpf
import mpl_finance as mpf

import tushare as ts
wdyx = ts.get_k_data('002739','2017-01-01')
wdyx.info()

# 对tushare获取到的数据转换成candlestick_ohlc()方法可读取的格式
data_list = []
for dates, row in hist_data.iterrows():
    # 将时间转换为数字
    date_time = datetime.datetime.strptime(dates, '%Y-%m-%d')
    t = date2num(date_time)
    open, high, low, close = row[:4]
    datas = (t, open, high, low, close)
    data_list.append(datas)

# 创建子图
fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)
# 设置X轴刻度为日期时间
ax.xaxis_date()
plt.xticks(rotation=45)
plt.yticks()
plt.title("股票代码：601558两年K线图")
plt.xlabel("时间")
plt.ylabel("股价（元）")
mpf.candlestick_ohlc(ax, data_list, width=1.5, colorup='r', colordown='green')
plt.grid()

'''
plt.figure(1)
x1= np.arange(-5.0, 5.0, 0.1)
plt.subplot(221)
plt.title('1')
plt.plot(np.sin(x1),np.cos(x1))
plt.subplot(222)
plt.title('2')
plt.plot(np.cos(x1))
plt.subplot(223)
plt.title('3')
plt.subplot(224)
plt.title('4')

plt.figure(2)
plt.plot(x1)


plt.show()
'''
