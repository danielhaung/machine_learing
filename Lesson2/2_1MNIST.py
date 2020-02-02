from keras.datasets import mnist 




(train_images, train_labels), (test_images, test_labels) = mnist.load_data()


#訓練資料
print(train_images.shape) #train_image為Numpy的ndarray物件，關於shape請看2-2-5節
#輸出 : (60000, 28, 28)     train_image的shape屬性為3軸，60000維 X 28維 X 28維
print(len(train_labels))    #60000 標籤也有60000個(一個 train image 對應一個 train label)
print(train_labels)

#測試資料
print(test_images.shape)    #(10000, 28, 28) 測試資料
print(len(test_labels))     #10000 標籤也有10000個(每個 test image 對應一個 test label)
print(test_labels)  #[7 2 1 ... 4 5 6]  標籤是 0-9 之間的數字
 

