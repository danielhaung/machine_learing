import numpy as np 

"""
純量(0D張量):純量就是只包含一個數值的張量
"""
# x = np.array(12)    #用12這個數值去建一個張量
# print(x)            #12   張量的內容原來Numpy的array就是tensor
# print(x.ndim)       #0   看看ndim屬性(就是階數)


"""
向量(1D張量)
"""
# x = np.array([12,3,6,14,7])    
# print(x)            
# print(x.ndim)      


"""
矩陣(2D張量)
"""
# x = np.array([[5, 78, 2, 34, 0],
#               [6, 79, 3, 35, 1],
#               [7, 80, 4, 34, 2]])
# print(x)            
# print(x.ndim) 


"""
(3D張量)和高階張量
"""
# x = np.array([[[5, 78, 2, 34, 0],
# [6, 79, 3, 35, 1],
# [7, 80, 4, 34, 2]],
# [[5, 78, 2, 34, 0],
# [6, 79, 3, 35, 1],
# [7, 80, 4, 34, 2]],
# [[5, 78, 2, 34, 0],
# [6, 79, 3, 35, 1],
# [7, 80, 4, 34, 2]]])

# print(x)            
# print(x.ndim)   



