import numpy as np
# quad = lambda x: (np.sum(x ** 2), x * 2)
# t = np.random.randint(low=1,high=3, size=(3,))
# print 't: ', t
# print quad(t)

x1 = [[2,4], 
      [1,3],
      [4,7]]
x1 = np.array(x1)
x2 = [[1,1]]
x2 = np.array(x2)
x = np.matmul(x1, x2)
print(x2.shape)
print(x.shape)