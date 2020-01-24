'''
Python科学计算——Numpy.genfromtxt:https://www.jianshu.com/p/82110f1dbb94
'''
import numpy as np 
data=np.genfromtxt("waveform.txt",delimiter=",",skip_header=8)
print(data[0:3,0], data[0:3,1])