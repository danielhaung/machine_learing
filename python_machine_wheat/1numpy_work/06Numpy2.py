import numpy


# #--------------------------------------------------------------------------------------------#
# #ndarray更改一個元素會牽動其他元素種類

# number = numpy.array([1,2,3,4])   #numpy.array這裡裡面必須是相同的結構
# print('內容：%s'%number)     
# print('種類dtype：%s'%number.dtype)

# number = numpy.array([1,2,3,4.0])  #改動其中一個元素，其它都會更正
# print('內容：%s'%number)
# print('種類dtype：%s'%number.dtype)

# number = numpy.array([1,2,3,'4'])  #改動其中一個元素，其它都會更正
# print('內容：%s'%number)
# print('種類dtype：%s'%number.dtype)


# #--------------------------------------------------------------------------------------------#
# #矩陣取值_1
# world_alcohol = numpy.genfromtxt("world_alcohol.txt",delimiter=',',dtype=str) #- genfromtxt函数创建数组表格数据
# print(world_alcohol)
# uruguay_other_1986 = world_alcohol[1,4]  #找行列上某一值
# print(uruguay_other_1986)
# third_country = world_alcohol[2,2]
# print(third_country)
# #--------------------------------------------------------------------------------------------#
# #矩陣取值_2  

vector = numpy.array([5,10,15,20])

matrix = numpy.array([
            [5,10,15],
            [20,25,30],
            [35,40,45]
        ])

# print(vector[0:3])
# print(matrix[:,1])
# print(matrix[:,0:2])    #:代表所有
# print(matrix[1:3,0:2])


# #--------------------------------------------------------------------------------------------#
#從陣列上判斷值 & 把布林值當作索引值
vector = numpy.array([5,10,15,20])
matrix = numpy.array([
            [5,10,15],
            [20,25,30],
            [35,40,45]
        ])
# print(vector ==10)  #判斷是否有元素等於10  
# print(matrix ==25)  #判斷是否有元素等於25

# #從陣列上判斷值後返回出來_1
# equal_to_ten = (vector ==10)
# print(equal_to_ten)
# print(vector[equal_to_ten])  #會把True的值返回
#從陣列上判斷值後返回出來_2
# second_column_25 = (matrix[:,1]==25)
# print(second_column_25)
# print(matrix[second_column_25,:])     #特別


# #--------------------------------------------------------------------------------------------#


