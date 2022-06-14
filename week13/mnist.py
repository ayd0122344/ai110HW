import torch
import torchvision
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import matplotlib.pyplot as plt
# from net_cnn2 import Net #【mynote】net_cnn2讓卷積層跟relu層變多，網路變大不見得是好事，可能會有overfitting的情況發生
# from net_fc import Net #【mynote】net_fc使用全連接，MLP的方式，此程式只有加入一層全連接層
from net_cnn1 import Net #【mynote】使用net_cnn1.py當作模型

def init(): #【mynote】初始化
    global n_epochs, batch_size_train, batch_size_test, learning_rate, momentum, log_interval
    n_epochs = 3
    batch_size_train = 64
    batch_size_test = 1000
    learning_rate = 0.01
    momentum = 0.5
    log_interval = 10
    random_seed = 1
    torch.backends.cudnn.enabled = False
    torch.manual_seed(random_seed)

def load_data(): #【mynote】載入資料
    global train_loader, test_loader
    train_loader = torch.utils.data.DataLoader(
    torchvision.datasets.MNIST('files/', train=True, download=True,
                                transform=torchvision.transforms.Compose([
                                torchvision.transforms.ToTensor(),
                                torchvision.transforms.Normalize(
                                    (0.1307,), (0.3081,))
                                ])),
    batch_size=batch_size_train, shuffle=True)

    test_loader = torch.utils.data.DataLoader(
    torchvision.datasets.MNIST('files/', train=False, download=True,
                                transform=torchvision.transforms.Compose([
                                torchvision.transforms.ToTensor(),
                                torchvision.transforms.Normalize(
                                    (0.1307,), (0.3081,))
                                ])),
    batch_size=batch_size_test, shuffle=True)

def show_examples(): #【mynote】顯示例子
    global test_loader
    examples = enumerate(test_loader)
    batch_idx, (example_data, example_targets) = next(examples)
    import matplotlib.pyplot as plt

    fig = plt.figure()
    for i in range(6):
        plt.subplot(2,3,i+1)
        plt.tight_layout()
        plt.imshow(example_data[i][0], cmap='gray', interpolation='none')
        plt.title("Ground Truth: {}".format(example_targets[i])) #【mynote】顯示標準答案
        plt.xticks([])
        plt.yticks([])

    plt.show()



def init_net(): #【mynote】初始化網路
    global network, optimizer, train_losses, train_counter, test_losses, test_counter
    network = Net()
    optimizer = optim.SGD(network.parameters(), lr=learning_rate,
                        momentum=momentum)
    train_losses = []
    train_counter = []
    test_losses = []
    test_counter = [i*len(train_loader.dataset) for i in range(n_epochs + 1)]

def train(epoch): #【mynote】開始訓練
    global network, optimizer, log_interval, train_losses, train_counter
    network.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        optimizer.zero_grad()
        output = network(data)
        loss = F.nll_loss(output, target)
        loss.backward()
        optimizer.step()
        if batch_idx % log_interval == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(train_loader.dataset),
                100. * batch_idx / len(train_loader), loss.item()))
            train_losses.append(loss.item())
            train_counter.append(
                (batch_idx*64) + ((epoch-1)*len(train_loader.dataset)))
            torch.save(network.state_dict(), 'results/model.pth')
            torch.save(optimizer.state_dict(), 'results/optimizer.pth')

def test(): #【mynote】測試正確率
    global network, test_loader
    network.eval()
    test_loss = 0
    correct = 0
    with torch.no_grad():
        for data, target in test_loader:
            output = network(data)
            test_loss += F.nll_loss(output, target, size_average=False).item()
            pred = output.data.max(1, keepdim=True)[1]
            correct += pred.eq(target.data.view_as(pred)).sum()
    test_loss /= len(test_loader.dataset)
    test_losses.append(test_loss)
    print('\nTest set: Avg. loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
        test_loss, correct, len(test_loader.dataset),
        100. * correct / len(test_loader.dataset)))

def show_result(): 
    global network, optimizer, train_losses, train_counter, test_losses, test_counter
    fig = plt.figure()
    plt.plot(train_counter, train_losses, color='blue')
    plt.scatter(test_counter, test_losses, color='red')
    plt.legend(['Train Loss', 'Test Loss'], loc='upper right')
    plt.xlabel('number of training examples seen')
    plt.ylabel('negative log likelihood loss')
    plt.show()

init()
load_data()
show_examples()
init_net()
test()
for epoch in range(1, n_epochs + 1): #【mynote】反覆訓練、測試
    train(epoch)
    test()
show_result() #【mynote】顯示結果
#【mynote】訓練好後的model存在results資料夾，下次要用的時候不需要重新學習