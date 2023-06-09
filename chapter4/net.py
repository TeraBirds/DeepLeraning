import sys, os
sys.path.append(os.pardir)
import numpy as np
from diff2 import numerical_gradient
from chapter3.soft_max import softmax
from sum_square import cross_entropy_error

class simpleNet:
  def __init__(self):
    self.W = np.random.randn(2,3)
  
  def predict(self, x):
    return np.dot(x, self.W)
  
  def loss(self, x, t):
    z = self.predict(x)
    y = softmax(z)
    loss = cross_entropy_error(y, t)
    return loss

x = np.array([0.6, 0.9])
t = np.array([0, 0, 1])

net = simpleNet()
print(net.loss(x, t))

f = lambda w: net.loss(x,t)
dW = numerical_gradient(f, net.W)

print(dW)
