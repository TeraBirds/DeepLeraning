import numpy as np
import matplotlib.pylab as plt
from diff2 import grad, func2

def de_grad(f, init_x, lr=0.1, step_num=100):
  x = init_x
  x_history = []
  
  for i in range(step_num):
    x_history.append(x.copy())
    gradiant = grad(f, x)
    x -= lr * gradiant
  
  return x, np.array(x_history)

if __name__ == "__main__":
  init_x = np.array([-3.0, 4.0])
  x, x_history = de_grad(func2, init_x=init_x, lr=0.1, step_num=100)
  print(x)
  
  plt.plot(x_history[:,0], x_history[:,1], "o")
  plt.xlim(-3.5, 3.5)
  plt.ylim(-4.5,4.5)
  plt.xlabel("x0")
  plt.ylabel("x1")
  plt.show()
