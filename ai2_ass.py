import numpy as np
a=np.array([
    [1,2,3],
    [2,4,8],
    [3,6,9]
])
#print(a)
'''b=np.hstack([a,a])
print(b)
c=np.vstack([a,a])
print(c)'''
m=a[:,-1:]
n=a[:,:1]
t=np.hstack([n,m])
print(t)
D=np.delete(a,1,1)
print('d=',D)