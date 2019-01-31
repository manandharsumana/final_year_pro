import numpy as np
import time
import matplotlib.pyplot as plt
data=np.loadtxt(fname='F:\python\inflammation-01.csv',delimiter=',')
#print(data)
'''print(type(data))
print(data.shape)
print('first number in array:',data[0,0])
print('middle number in array:',data[20,30])
print(data[0:4,0:10])
print('next data:')
print(data[5:10,0:10])
print('next data:')
print(data[0:3,36:])
d=data*2
print('the double data:',d[0:3,36:])
tripledata=d+data
print('the triple data:',tripledata[0:3,36:])

print('the mean of data:',np.mean(data))
print('the current time:',time.ctime())
maxval,minval,stdval=np.max(data),np.min(data),np.std(data)
print('the minimum value:',minval)
print('the maximum value:',maxval)
print('the standard value:',stdval)
print('the maximum inflammation in patient 0:',np.max(data[0,0:]))
print('the maximum inflammation in patient 2:',np.max(data[2,0:])
print('average inflammation per day of allpatient:',np.mean(data,axis=1))
#visualizing data
image=plt.imshow(data)
plt.show()
average_val=np.mean(data,axis=0)
avg=plt.plot(average_val)
plt.show()
max_val=np.min(data,axis=0)
maxx=plt.plot(max_val)
plt.show()'''
fig=plt.figure(figsize=(10,3))
axis1=fig.add_subplot(1,3,1)
axis2=fig.add_subplot(1,3,2)
axis3=fig.add_subplot(1,3,3)
axis1.set_ylabel('average')
axis1.plot(np.mean(data,axis=0))
axis2.set_ylabel('maximum')
axis2.plot(np.max(data,axis=0))

axis3.set_ylabel('minimum')
axis3.plot(np.min(data,axis=0))
axis3.set_ylim(0,6)
#fig.tight_layout()
plt.show()
'''element='oxygen'
print(element[1:-1])
print(data[3:3,:])'''