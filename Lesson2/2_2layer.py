#神經網路架構
"""
在程式中由兩個密集層(Dense Layers)緊密連接組成的，密集層也稱為"全連接(fully connected)"神經層
"""
from keras import models 
from keras import layers

network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
network.add(layers.Dense(10, activation='softmax' )) 