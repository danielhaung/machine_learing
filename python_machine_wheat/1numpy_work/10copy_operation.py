import numpy as np 
# ------------------------------------------------------------------------------#
# 簡單賦值不會復制數組對像或其數據
# a = np.arange(12)
# b = a
# # a和b是同一個ndarray對象的兩個名稱
# print(b is a )
# b.shape=(3,4)
# print(a.shape)
# print(id(a))
# print(id(b))


# # ------------------------------------------------------------------------------#
# #view方法創建一個查看相同數據的新數組對象(淺複製)
# a = np.arange(12)
# c=a.view()
# print(c is a)
# c.shape=(2,6)
# print(a.shape)
# c[0,4]=1234
# print(a)  #1234被複製過來的 雖然是不同矩陣 但是共用數值有關
# print(c)
# print(id(a))
# print(id(c))  #不同id
# # ------------------------------------------------------------------------------#

# #copy方法生成數組及其數據的完整副本(深複製)
# a = np.arange(12)
# a.shape = (3,4)
# d = a.copy()
# print(d is a) #False
# d[0,0] = 9999
# print(d)
# print(a) #兩個完全是不一樣的東西

# #------------------------------------------------------------------------------#
# data = np.sin(np.arange(20)).reshape(5,4)
# print(data)
# ind = data.argmax(axis=0)  #找索引最大的位置 axis=0 按列計算
# print(ind)
# print(data.shape[1])    #(5, 4)中的4
# data_max = data[ind, range(data.shape[1])]  #range(data.shape[1] 代表第一行開始哪個列數字最大
# print(data_max)

# #------------------------------------------------------------------------------#
# #擴展
# a = np.arange(0, 40, 10)
# print(a)
# b = np.tile(a,(2,2))  #擴展a 成多個矩陣組合
# print(b.shape)
# print(b)

# # ------------------------------------------------------------------------------#
a = np.array([[4,3,5],[1,2,1]])
print(a)
print("---------------------")
b = np.sort(a,axis=1)
print(b)
a.sort(axis=1)
print("---------------------")
print(a)
a = np.array([4,3,1,2])
j = np.argsort(a)  #排列出最大值的到最小值的索引
print("---------------------")
print(j)
print("---------------------")
print(a[j])


