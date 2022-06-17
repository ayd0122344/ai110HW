from keras.datasets import mnist
import keras
import numpy as np
from keras.utils import np_utils
from engine import Value

(x_train,y_train),(x_test,y_test) = mnist.load_data() # 載入資料
train_images = np.asarray(x_train, dtype=np.float32) / 255.0 # np.asarray用於將list轉換為數組，如設置dtype，僅當dtype不匹配時才複製數組。
test_images = np.asarray(x_test, dtype=np.float32) / 255.0 #數字標準化可以提高後續訓練模型的準確率，因為image的數字是0到255，所以最簡單標準化的方式是除以255。
train_images = train_images.reshape(60000,784) # 將原本28*28的2維數字影像，以reshape轉換為1維的向量，共784個float數字。
test_images = test_images.reshape(10000,784)

y_train = np_utils.to_categorical(y_train) # 標籤(圖像的答案:0,1,2,...9)做onehot encoding


def calculate_loss(X,Y,W):
  
  return -(1/X.shape[0])*np.sum(np.sum(Y*np.log(np.exp(np.matmul(X,W)) / np.sum(np.exp(np.matmul(X,W)),axis=1)[:, None]),axis = 1))

batch_size = 32 # 批次大小設32
steps = 20000 # 訓練20000次
Wb = Value(np.random.randn(784,10)) # 重新初始化梯度下降的權重 # np.random.randn(784,10)建立一個784 x 10的矩陣，並且隨機給它數值
for step in range(steps):
  ri = np.random.permutation(train_images.shape[0])[:batch_size] # train_images.shape[0]輸出矩陣行數(也就是60000) # np.random.permutation(value)輸出一串包含0~value的數字隨機排列之陣列。
  # 所以ri是把一個0~59999的陣列重新洗牌後，再從中挑出前batch_size個
  Xb, yb = Value(train_images[ri]), Value(y_train[ri]) # train_images[ri]和y_train[ri]繼承Value並分別放在Xb和yb
  y_predW = Xb.matmul(Wb) # Wb傳入Xb的matmul運算後存在y_predW
  probs = y_predW.softmax() # y_predW做softmax後放在probs
  log_probs = probs.log() # probs做log後放在log_probs

  zb = yb*log_probs

  outb = zb.reduce_sum(axis = 1) # zb降回一維後放在outb
  finb = -outb.reduce_sum()  #cross entropy loss # 計算outb的總和後乘上-1，放在finb
  finb.backward() # 對finb做反傳遞
  if step%1000==0: # 如果已經訓練1000個就計算loss並印出
    loss = calculate_loss(train_images,y_train,Wb.data)
    print(f'loss in step {step} is {loss}')
  Wb.data = Wb.data- 0.01*Wb.grad # 做微調
  Wb.grad = 0 # 梯度設0後繼續下一次訓練
loss = calculate_loss(train_images,y_train,Wb.data) # 已經全部訓練好了，但最後一1000次沒有計算loss並印出，所以這邊計算loss
print(f'loss in final step {step+1} is {loss}') # 算好loss後印出

from sklearn.metrics import accuracy_score # 使用準確率
print(f'accuracy on test data is {accuracy_score(np.argmax(np.matmul(test_images,Wb.data),axis = 1),y_test)*100} %')