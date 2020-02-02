def naive_add_matrix_and_vector(x, y):
    assert len(x.shape) == 2 # x 是一個2D Numpy 張量
    assert len(y.shape) == 1 # y 是一個 Numpy 張量
    assert x.shape[1] == y.shape[0]
    x = x.copy()    #避免複寫到輸入張量
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i, j] += y[j]
    return x





import numpy as np


# #######################################################
# #一般的方式

# x = np.array([[1,2,3],
#             [4,5,6]])

# y = np.array([1,2,3])
# #print(naive_add_matrix_and_vector(x, y))

# #######################################################
# #透過 Numpy 張量擴張

# x = np.random.random((64, 3, 32, 10))   # x 是一個隨機張量,shape為(64,3,32,10)
# y = np.random.random((32, 10))   # yx 是一個隨機張量,shape為(32,10)

# z = np.maximum(x,y)
# print(z.shape)      #輸出結果z的shape就如同x一樣是(64,3,32,10),意思是y已先被擴張了


