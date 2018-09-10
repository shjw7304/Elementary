# DataFrame 学习

import pandas as pd
import numpy as np

# 创建DataFrame对象
df = pd.DataFrame([1, 2, 3, 4, 5], columns=['cols'], index=['a','b','c','d','e'])
print (df)


df2 = pd.DataFrame([[1, 2, 3],[4, 5, 6]], columns=['col1','col2','col3'], index=['a','b'])
print (df2)


df4 = pd.DataFrame({'col1':[1,3],'col2':[2,4]},index=['a','b'])
print (df4)
