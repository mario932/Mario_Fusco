import numpy as np
a = np.matrix('1 2; 3 4')
b = np.matrix('8 7; 5 6')
print(a)
print(b)

print (a*b)
print(np.dot(a,b))