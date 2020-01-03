"""
rule的算法
"""
def naive_relu(x):
    assert len(x.shape) == 2 #若x不是2D張量，將會發生AssertionError
    
    x = x.copy()    #避免覆寫到輸入張量
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i,j] = max(x[i,j],0)  #若元素小於0則設定為0,若大於0則維持原數值
    return x 

#元素間相加
def naive_add(x,y):
    assert len(x.shape) == 2   
    assert x.shape == y.shape

    x = x.copy()
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i,j] += y[i,j]
    return x


import numpy as np

b =np.array([[-1],[2]])
# print(len(b.shape))
print(naive_relu(b))
x = np.array([[1],[2]])
y = np.array([[3],[4]])
print(naive_add(x,y))

z = x + y
print(z)
z = x * y
print(z)
z = np.maximum(z, 0.)
print(z)

