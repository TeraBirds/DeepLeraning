import numpy as np
import matplotlib.pylab as plt


def numerical(f, x):
  """数値微分を行う関数

  Args:
      f (_type_): 関数f(x)
      x (_type_): 微分したいx

  Returns:
      微分値
  """
  h = 1e-4  #0.001
  return (f(x+h)-f(x-h)) / (2*h)

def func1(x):
  return 0.01*x**2 + 0.1*x

if __name__ == "__main__":
  x = np.arange(0.0, 20.0, 0.1) #０から２０まで、０.１刻みのx配列
  y = func1(x)

  print(numerical(func1, 5))
  print(numerical(func1, 10))

  plt.xlabel("x")
  plt.ylabel("f(x)")
  plt.plot(x, y)
  plt.show()
