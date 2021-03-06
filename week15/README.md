
# 機器學習

## 第一堂

* 主要是在尋找函數

* 函數分為regression(用於預測)、classification(用於分類)

* 定義損失函數，以往會使用最小平方法，對於預測類別可能會使用softmax或cross entropy

* 以前激勵函數會使用sigmoid，因其效區不大，現在多使用relu

## 第二堂

* 我們希望訓練集loss小，測試集loss小

* 訓練集本身loss大，有可能是:
    1. 模型不好，模型不對
    2. 模型OK，但演算法(梯度下降法)不好

* 訓練集本身loss小，但測試集loss大，有可能是:
    1. overfitting
    2. mismatch，訓練資料跟測試資料有明顯差異，如資料類型不一

* 我們不希望overfitting或找不到結果，會從比較淺的網路慢慢加深

* 圖像測試資料如果不夠多，可以考慮把照片左右翻轉，或擷取圖像中的一部份

* 交叉驗證

    * 將訓練集在分成訓練集跟驗證集，當訓練集跟驗證集的loss都越來越小，可以繼續訓練
    * 但是當訓練集的loss都越來越小，驗證集loss越來越大的時候就要停止。

## 第三堂

* 鞍點在高維空間不常出現

* 可以透過批次或增加動量的方式來通過鞍點

* 不要一次把所有的樣本都拿來，每次取得的是不同批次樣本，有助於挑脫鞍點的問題

* 有一定的批量，批量不要太大，速度快又好