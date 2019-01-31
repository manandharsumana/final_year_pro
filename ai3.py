import numpy as np
import matplotlib.pyplot as plt
X=np.array([1,2,4,3,5])
y=np.array([1,3,3,2,5])
sx=0
s=0

for i in range(5):
    sx=sx+((X[i]-np.mean(X))*(y[i]-np.mean(y)))
    s=s+(X[i]-np.mean(X))**2
B1=sx/s
print(B1)
B0=np.mean(y)-B1*np.mean(X)
#print(sx)
#print(s)
Y_hat=B0+B1*X
RMSE=np.sqrt((((Y_hat-y)**2).sum())/len(X))

print(RMSE)
plt.scatter(X,y,color='r')
plt.plot(X,Y_hat)
plt.show()
