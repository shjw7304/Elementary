
import numpy as np

x=[1,2,3,4]
print("mean:",np.mean(x))
print("cov:",np.cov(x))

x=[1,2,3,4]
y=[1,1,1,1]

# x = np.array([[1, 5, 6], [4, 3, 9], [4, 2, 9], [4, 7, 2]])
print(np.cov(x,y))
