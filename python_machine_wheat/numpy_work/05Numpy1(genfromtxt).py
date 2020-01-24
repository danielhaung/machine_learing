import numpy

# #----------------------------------------------------------------------------------------------------------------#
# #練習匯入檔案
# world_alcohol = numpy.genfromtxt("world_alcohol.txt",delimiter=',',dtype=str,skip_header=1)#delimiter横纵坐标以 ',' 分割 #- genfromtxt函数创建数组表格数据,skip_header) skip_header:有用数据是从x行开始的，因此给 skip_header 传入x-1
# #- genfromtxt主要执行两个循环运算。第一个循环将文件的每一行转换成字符串序列。第二个循环将每个字符串序列转换为相应的数据类型。
# print(type(world_alcohol))  #<class 'numpy.ndarray'> 
# print(world_alcohol)
# #print(help(numpy.genfromtxt))  

# #----------------------------------------------------------------------------------------------------------------#

# vector = numpy.array([5,10,15,20])
# matrix = numpy.array([[5,10,15],[20,25,30],[35,40,45]])
# print(vector)
# print(matrix)
# print(vector.shape)
# print(matrix.shape)
"""
python中的list和array的不同之處：https://blog.csdn.net/liyaohhh/article/details/51055147
"""














