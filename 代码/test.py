# 矩阵公式
import numpy as np

a = np.array([[1,2,3],[4,5,6]])
print(a)
b = np.array([[1,2],[3,4],[5,6]])
c = np.array([[1,2,3]])
d = np.array([[9,8,7],[3,2,1]])

# 矩阵加法
sum = a + d
print(sum)

#数乘，矩阵乘
e = np.dot(a,b)

#元素乘  矩阵对应位置相乘
e = a * d

# 转置
e = c.T
print(e)
e = np.array([[1,2],[3,4]])

#逆矩阵
result = np.linalg.inv(e)
print(result)
#计算矩阵转行列式的值
result = np.linalg.det(e)
print(result)

#矩阵的秩
e = np.linalg.matrix_rank(d)
print(e)

