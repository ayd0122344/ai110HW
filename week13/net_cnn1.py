import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        #【mynote】使用一層卷積+一層線性層
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5) 
        self.fc1 = nn.Linear(10*12*12, 10)

    def forward(self, x):
        x = F.relu(F.max_pool2d(self.conv1(x), 2)) # 維度: 1*(28*28)=>10*(24*24)/2=>10*(12*12) #【mynote】一層卷積+一層pool+一層relu
        x = x.view(-1, 10*12*12) #【mynote】攤平
        x = self.fc1(x) #【mynote】做全連接
        return F.log_softmax(x) #【mynote】使用softmax計算當作目標函數
