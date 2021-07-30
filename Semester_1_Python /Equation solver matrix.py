import numpy as np
a=np.array([[1,2,3,4],[9,3,4,5],[7,4,5,6],[2,3,1,7]])   #matrix with coefficients of variables
inv=np.linalg.inv(a)
b=([1,2,3,4])
result=np.matmul(b,inv)
print(result)
