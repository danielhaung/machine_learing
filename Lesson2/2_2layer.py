#神經網路架構
"""
在程式中由兩個密集層(Dense Layers)緊密連接組成的，密集層也稱為"全連接(fully connected)"神經層
"""
from keras import models 
from keras import layers


network = models.Sequential()   #您可以Sequential通過將一系列圖層實例傳遞給構造函數來創建模型。https://keras.io/getting-started/sequential-model-guide/
#第一層                            #您還可以通過.add()方法簡單地添加圖層
network.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))   
#第二層
network.add(layers.Dense(10, activation='softmax' )) #這層可以輸出一個含有10個機率評分(probability scores)的陣列(機率總合為1)






