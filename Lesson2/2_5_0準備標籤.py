#編譯步驟
"""
在程式中由兩個密集層(Dense Layers)緊密連接組成的，密集層也稱為"全連接(fully connected)"神經層
"""
from keras.datasets import mnist 
from keras import models 
from keras import layers
from keras.utils import to_categorical  #to_categorical:將類向量（整數）轉換為二進制類矩陣。




(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
network.add(layers.Dense(10, activation='softmax' )) 

network.compile(optimizer = 'rmsprop',              #指定優化器
                loss = 'categorical_crossentropy',  #指定損失函數
                metrics = ['accuracy'])             #指定評量準則


#2-4轉換格式        
#reshape和astype是NumPy陣列的method
train_images = train_images.reshape((60000,28*28))
train_images = train_images.astype('float32') / 255

test_images = test_images.reshape((10000, 28*28))
test_images = test_images.astype('float32') / 255


#2_5準備標籤
#對標籤進行分類編碼
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)


#fit : 為模型訓練固定的紀元（數據集上的迭代）。
network.fit(train_images, train_labels, epochs=5,batch_size=128)  #epochs:疊代層數  batch_size:批次處理https://keras.io/models/model/#fit
test_loss, test_acc = network.evaluate(test_images, test_labels)    #evaluate : 返回測試模式下模型的損失值和指標值
print('test_acc:',test_acc)


