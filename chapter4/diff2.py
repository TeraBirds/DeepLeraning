import numpy as np
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D
from diff import numerical



def func2(x):
  if x.ndim == 1:
    return np.sum(x**2)
  else:
    return np.sum(x**2, axis=1)



def numerical_gradient(f, x):
    h = 1e-4 # 0.0001
    grad = np.zeros_like(x)
    
    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
    while not it.finished:
        idx = it.multi_index
        tmp_val = x[idx]
        x[idx] = tmp_val + h
        fxh1 = f(x) # f(x+h)
        
        x[idx] = tmp_val - h 
        fxh2 = f(x) # f(x-h)
        grad[idx] = (fxh1 - fxh2) / (2*h)
        
        x[idx] = tmp_val # 値を元に戻す
        it.iternext()   
        
    return grad


def tangent_line(f, x):
  """接線を与える関数

  Args:
      f (_type_): 関数
      x (_type_): 接線を与えたいxの値

  Returns:
      _type_: 接線の関数
  """
  d = grad(f, x)  #勾配
  print(d)
  y = f(x) - d*x
  return lambda t: d*t + y

if __name__ == "__main__":
  print (grad(func2, np.array([3.0, 4.0])))
  print (grad(func2, np.array([0.0, 2.0])))
  print (grad(func2, np.array([3.0, 0.0])))
  
  x0 = np.arange(-3, 3, 0.1)
  x1 = np.arange(-3, 3, 0.1)
  X, Y = np.meshgrid(x0, x1)
  
  X = X.flatten()
  Y = Y.flatten()
  
  grad = grad(func2, np.array([X, Y]).T).T
  
  plt.figure()
  plt.quiver(X, Y, -grad[0], -grad[1],  angles="xy",color="#666666")
  plt.xlim([-3, 3])
  plt.ylim([-3, 3])
  plt.xlabel('x0')
  plt.ylabel('x1')
  plt.grid()
  plt.draw()
  plt.show()
  
