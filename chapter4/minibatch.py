import numpy as np
import sys, os
sys.path.append(os.pardir)
from dataset.mnist import load_mnist
from sum_square import cross_entropy_error

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

print("入力のxは6000個x784ピクセル")
print(x_train.shape)
print("出力のtは6000個x10通り")
print(t_train.shape)

#訓練データからランダムに抜き出す
train_size = x_train.shape[0]
batch_size = 10
batch_mask = np.random.choice(train_size, batch_size)
x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]

print(x_batch)
print(t_batch)

#以下で損失関数を計算(公差エントロピー誤差)
