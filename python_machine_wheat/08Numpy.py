import numpy as np

# #-------------------------------------------------------------------
# #把列表變成指定行列
# print(np.arange(15))
# a = np.arange(15).reshape( 3 ,5)
# print(a)
# a.size #15有15個元素
# a.dtype.name #'int32'
# #-------------------------------------------------------------------
# #初始化矩陣
# print(np.zeros((3,4))) #初始化一個0的矩陣(元組)
# print(np.ones((2,3,4),dtype=np.int32))  #2個3x4的矩陣
# #生成矩陣
# print(np.arange(10,30,5))  #初始值10 每隔5 到30以前結束
# print(np.arange(12).reshape(4,3))
# #運用random生成隨機-1~1的矩陣
# print(np.random.random((2,3)))
# from numpy import pi
# print(np.linspace(0,2*pi,100))   #0終點值是2pi  取100個值 會自動分配間距
# #-------------------------------------------------------------------
# #the product operator*operates elementwise in NumPy arrays
# a=np.array([20,30,40,50])
# b = np.arange(4)
# print(a)
# print(b)
# c=a-b
# print(c)
# c=c-1 #會對每一個元素做減法
# print(c)
# b**2    #會對每一個元素做平方
# print(b**2)
# print(a<35) #顯示True or False
# #-------------------------------------------------------------------
# #The matrix product can be performed using the dot function or method可以使用dot函數或方法來執行矩陣乘積
# A =np.array(
#     [[1,1],
#     [0,1]]
# )
# B = np.array(
#     [[2,0],
#     [3,4]]
# )
# print('---A----')
# print(A)
# print('---B----')
# print(B)
# print('----A*B---')
# print(A*B)  #對應元素相乘
# print('---A.dot(B)----')
# print(A.dot(B))  #內積
# print('---np.dot(A,B)----')
# print(np.dot(A,B))#內積 跟上面一樣






