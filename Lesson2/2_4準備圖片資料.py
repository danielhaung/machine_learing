#編譯步驟
"""
在程式中由兩個密集層(Dense Layers)緊密連接組成的，密集層也稱為"全連接(fully connected)"神經層
"""
from keras.datasets import mnist 
from keras import models 
from keras import layers

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
network.add(layers.Dense(10, activation='softmax' )) 

network.compile(optimizer = 'rmsprop',              #指定優化器
                loss = 'categorical_crossentropy',  #指定損失函數
                metrics = ['accuracy'])             #指定評量準則


#2-6轉換格式        
train_images = train_images.reshape((60000,28*28))
train_images = train_images.astype('float32') / 255

test_images = test_images.reshape((10000, 28*28))
test_images = test_images.astype('float32') / 255