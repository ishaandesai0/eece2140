import numpy as np
import math

i = .5
vector = []

while i <= 5:
    
    b = 0
    n = 0
    x = 0
    y = 0
    k = 0
    count = 0
    
    nO = 10 * math.log(10, 10) * i
    linearNO = 10 ** (nO/10)
    
    b = np.round(np.random.rand(1000))
    n = np.random.randn(1000)*np.sqrt(linearNO/2)
    
    x = 2*b-1
    y = x + n
    