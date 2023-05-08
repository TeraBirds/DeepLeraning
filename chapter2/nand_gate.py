import numpy as np
def nand_gate(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    y = np.sum(w*x) + b
    
    if y <= 0:
        print(0)
    else:
        print(1)

def or_gate(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    y = np.sum(w*x) + b
    
    if y <= 0:
        print(0)
    else:
        print(1)


nand_gate(0, 0)
nand_gate(0, 1)
nand_gate(1, 0)
nand_gate(1, 1)

or_gate(0, 0)
or_gate(0, 1)
or_gate(1, 0)
or_gate(1, 1)