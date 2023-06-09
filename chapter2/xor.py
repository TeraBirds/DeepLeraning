import numpy as np
def and_gate(x1, x2):
  x = np.array([x1, x2])
  w = np.array([0.5, 0.5])
  b = -0.7
  y = np.sum(w*x) + b
  
  if y <= 0:
    return 0
  else:
    return 1

def nand_gate(x1, x2):
  x = np.array([x1, x2])
  w = np.array([-0.5, -0.5])
  b = 0.7
  y = np.sum(w*x) + b
  
  if y <= 0:
    return 0
  else:
    return 1

def or_gate(x1, x2):
  x = np.array([x1, x2])
  w = np.array([0.5, 0.5])
  b = -0.2
  y = np.sum(w*x) + b
  
  if y <= 0:
    return 0
  else:
    return 1


#xorゲートの実装
def xor_gate(x1, x2):
  s1 = nand_gate(x1, x2)
  s2 = or_gate(x1, x2)
  y = and_gate(s1, s2)
  print(y)

xor_gate(0, 0)
xor_gate(0, 1)
xor_gate(1, 0)
xor_gate(1, 1)