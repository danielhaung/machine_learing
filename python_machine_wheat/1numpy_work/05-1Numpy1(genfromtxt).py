'''
Python科学计算——Numpy.genfromtxt:https://www.jianshu.com/p/82110f1dbb94
skip_header=8  -> 從第八行開始
'''
import numpy as np 
data=np.genfromtxt("waveform.txt",delimiter=",",skip_header=7)
# print(data)
print(data[0:3,0])
# print(data[0:3,0], data[0:3,1])