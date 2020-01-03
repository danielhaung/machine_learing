"""
1. 軸的數量
2. 形狀
3. 資料型別
"""

from keras.datasets import mnist 

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()


######################################################
print(train_images.ndim)
print(train_images.shape)
print(train_images.dtype)

digit = train_images[4]

import matplotlib.pyplot as plt 
plt.imshow(digit, cmap=plt.cm.binary)

plt.show()


######################################################
"""
在Numpy做張量切片Tensor Slicing
"""
# my_slice = train_images[10:100] 
# print(my_slice.shape)
# my_slice = train_images[10:100,:,:] #相等於上面寫法
# print(my_slice.shape)
# my_slice = train_images[10:100,0:28,0:28] #相等於上面寫法
# print(my_slice.shape)   #(90, 28, 28)

##顯示出所有影像中右下角的14 X 14 像素，可執行以下指令
# my_slice = train_images[:,14:,14:]  #這裡的 14: 就等於 14:28
# print(my_slice.shape)
 
##7:-7是從頭7個元素到-7個元素，但不含-7,所以0到6和-7到-1前後各7個元素被去掉了，剩下中間的14X14像素
# my_slice = train_images[:,7:-7,7:-7] 
# print(my_slice.shape)


