import matplotlib.pyplot as plt
import numpy as np

#plt.figure(1, figsize=(4,4))

plt.figure(1,figsize=(1,1))
# 只传入一个参数的话, 默认为y轴, x轴默认为range(n)
# axis()指定坐标轴的取值范围 [xmin, xmax, ymin, ymax], 注意传入的是一个列表即:axis([])
plt.subplot(211)
plt.axis([-1, 4, -1, 5])
plt.plot([1,2,3])
plt.title("plt.plot([1,2,3])")

# ro 表示点的颜色和形状, 默认为 'b-'
plt.subplot(212)
plt.axis([-1, 4, -1, 5])
plt.plot([1,2,3], 'ro')
plt.title("plt.plot([1,2,3],'ro')")

plt.figure(2, figsize=(4,4))

# plot可以一步画出多条线,不过没法设置其他的line properties
plt.axis([0, 6, 0, 20])
x = np.arange(0, 4, 0.08)
#plt.plot(x, x, 'r--', x, np.power(x,2), 'bs',x, np.power(x,3), 'g^')

plt.plot(x, x, 'r--')
plt.plot(x, np.power(x,2), 'bs')
plt.plot(x, np.power(x,3), 'g^')


plt.show()