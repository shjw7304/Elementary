import numpy as np
import matplotlib.pyplot as plt

#3
ax = plt.subplot(111)
t = ax.text(1, 1.5, 'text')
plt.setp(t)
plt.setp(t, 'color') # 输出为:color: any matplotlib color
plt.setp(t, color='indigo')
#4
plt.title(r'$\sigma_i=15$') # 即σi
#5
x = np.arange(0, 5, 0.02)
y = np.cos(2*np.pi*x)
plt.plot(x, y, lw=2.0)
plt.ylim(-2,2)

# xy : 图上需要标注的点, xytext: 对标记点进行说明的文本
# arrowsprops: 标记方式 其中shrink为箭头的长度(shrink越小越长)
a = plt.annotate('local max', xy=(2,1), xytext=(3,1.5),arrowprops=dict(facecolor='k', shrink=0.02),)

plt.show()