def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    y = x1*w1 + x2*w2
    
    if y <= theta:
        print(0)
    else:
        print(1)


#重みとバイアスによる方式
import numpy as np
def and_gate(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    y = np.sum(w*x) + b
    
    if y <= 0:
        print(0)
    else:
        print(1)

and_gate(0, 0)
and_gate(1, 0)
and_gate(0, 1)
and_gate(1, 1)
