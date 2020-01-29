import numpy

# #----------------------------------------------------------------------------------------------------------------#
#練習匯入檔案
#genfromtxt : 從文本文件加載數據，並按指定方式處理缺少的值。
# world_alcohol = numpy.genfromtxt("world_alcohol.txt",delimiter=',',dtype=str,skip_header=0)#delimiter横纵坐标以 ',' 分割 #- genfromtxt函数创建数组表格数据,skip_header) skip_header:有用数据是从x行开始的，因此给 skip_header 传入x-1
# # - genfromtxt主要执行两个循环运算。第一个循环将文件的每一行转换成字符串序列。第二个循环将每个字符串序列转换为相应的数据类型。
# print(type(world_alcohol))  #<class 'numpy.ndarray'> 
# print(world_alcohol)
#print(help(numpy.genfromtxt))  #出現幫助文檔

# #----------------------------------------------------------------------------------------------------------------#

# vector = numpy.array([5,10,15,20])
# matrix = numpy.array([[5,10,15,1],[20,25,30,1],[35,40,45,1]])
# print(vector)
# print(matrix)
# print(vector.shape)
# print(matrix.shape) #shape的(3, 4)就像是有三個資料裡面每個資料有四個資料
"""
python中的list和array的不同之處：https://blog.csdn.net/liyaohhh/article/details/51055147
 python中的list是python的内置数据类型，list中的数据类不必相同的，而array的中的类型必须全部相同。在list中的数据类型保存的是数据的存放的地址，简单的说就是指针，并非数据，这样保存一个list就太麻烦了，例如list1=[1,2,3,'a']需要4个指针和四个数据，增加了存储和消耗cpu。

      numpy中封装的array有很强大的功能，里面存放的都是相同的数据类型

"""














