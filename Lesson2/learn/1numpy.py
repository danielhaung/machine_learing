"""
ndarray的關鍵屬性是維度(ndim)、形狀(shape)、和數值類型(dtype)
"""

#引入 numpy 模組
import numpy as np 
np1 = np.array([1,2,3])
np2 = np.array([3,4,5])

#陣列相加
print(np1 + np2)    #[4,5,6]

#顯示相關資訊
print(np1.ndim, np1.shape , np1.dtype)  # 1 (3,) int64 => 一維陣列, 三個元素, 資料型別


#改變維度
np3 = np.array([1, 2, 3, 4, 5, 6])
np3 = np3.reshape([2,3])
print(np3.ndim, np3.shape , np3.dtype)
print(np3.shape[0],len(np3.shape))


np4 = np.array([-1,2])
print(np4.shape)
print(len(np4.shape))



