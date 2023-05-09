import numpy as np

def soft_max(a):
  exp_a = np.exp(a)
  sum_exp_a = np.sum(exp_a)
  y = exp_a / sum_exp_a
  
  return y

def softmax(a): #オーバーフロー対策を施した関数
  c = np.max(a)
  exp_a = np.exp(a - c)
  sum_exp_a = np.sum(exp_a)
  y= exp_a / sum_exp_a
  
  return y
