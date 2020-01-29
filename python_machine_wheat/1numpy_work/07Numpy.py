
import numpy
# #------------------------------------------------------------------------
# #We can also perform comparisons with multiple conditions
# 我們還可以與多個條件進行比較
# #and &
# vector = numpy.array([5,10,15,20])
# equal_to_ten_and_five = (vector ==10) & (vector ==5)
# print(equal_to_ten_and_five)  #[False False False False]
# #or |
# vector = numpy.array([5,10,15,20])
# equal_to_ten_and_five = (vector ==10) | (vector ==5)
# print(equal_to_ten_and_five)  #[ True  True False False]

# #------------------------------------------------------------------------
# #we can convert the date type of an array with the ndarray. astype() method.
# 我們可以用ndarray轉換數組的數據類型。 astype（）方法。
# vector = numpy.array(["1","2","3"])
# print(vector.dtype)
# print(vector)
# vector=vector.astype(float)
# print(vector.dtype)
# print(vector)

# #------------------------------------------------------------------------
# #看最小值
# vector =numpy.array([5,10,15,20])
# print(vector.min())
# print(vector.max())

# #------------------------------------------------------------------------
# #The axis dictates which dimension we perform the operation on 軸指示我們執行操作的維度
# #1 means that we want to perform the operation on each row , and 0 means on each column
# matrix = numpy.array([
# [5,10,15],[20,25,30],[35,40,45]
# ])
# print(matrix.sum(axis=1))  #行加行
# print(matrix.sum(axis=0))  #列加列

# #------------------------------------------------------------------------
