def naive_vector_dot(x, y):
    assert len(x.shape) == 1
    assert len(y.shape) == 1 # x 與 y 是Numpy向量
    assert x.shape[0] == y.shape[0]
    z = 0
    for i in range(x.shape[0]):
        z += x[i] * y[i]        #就是 x[0] * y[0] + x[1] * y[1] + x[1] * y[1]+ x[2] * y[2]
    return z


import numpy as np



##################################
#兩個向量點乘
x = np.array([1,1,1])
y = np.array([1,2,3])

# print(naive_vector_dot(x,y))

##################################
#一矩陣一向量點乘

def naive_matrix_vector_dot(x, y):
    assert len(x.shape) == 2    # x 是Numpy矩陣
    assert len(y.shape) == 1    # y 是Numpy向量
    assert x.shape[1] == y.shape[0] # x 的第一軸的維數必須與y第0軸的維度相等
#or
    z = np.zeros(x.shape[0]) 
    for i in range(x.shape[0]):
        z[i] = naive_vector_dot(x[i,:], y)
        
#or
    # z = np.zeros(x.shape[0])    # z 為與 x 第0軸形狀一樣，數值為0的向量
    # for i in range(x.shape[0]):
    #     for j in range(x.shape[1]):
    #         z[i] += x[i, j] * y[j]  # z 的各元素已被內層for loop 填入了

    return z 


x = np.array([[1,1,1],[1,1,1]])
y = np.array([1,2,3])

# print(naive_matrix_vector_dot(x,y))



##################################
#矩陣與矩陣之間的點積

def naive_matrix_dot(x, y):
    assert len(x.shape) ==  2
    assert len(y.shape) ==  2
    assert x.shape[1] == y.shape[0] # x與y是Numpy矩陣，x 的第1維的數量必須與y第0維的數量相等

    z = np.zeros((x.shape[0], y.shape[1]))  #這裡會建立數值為 0 的矩陣
    for i in range(z.shape[0]):
        for j in range(y.shape[1]): #重複計算 x 各列數值與 y 各行數值
            row_x = x[i, :]
            column_y = y[:, j]
            z[i, j] = naive_vector_dot(row_x, column_y)
    return z 

x = np.array([[1,1],[1,1],[1,1]])
y = np.array([[1,2,3],[1,1,1]])
# print(naive_matrix_dot(x, y))


