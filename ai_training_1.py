import numpy as np
sum=np.random.uniform(0,1,size=(50,3))
#print (x)
y=[1,4,3]
sum=sum+y
#print(sum)
Q=np.insert(sum,3,1,1)
#print(p)
#first camera
P1 = [ [1, 0, 0, 0], [0, 1, 0, 0], [0, 0 ,1, 0]]

#m=np.transpose(Q)
q = np.dot(P1,Q.T)
q = np.transpose(q)
print(q)
u1 = q[:,0]/q[:,2]
v1 = q[:,1]/q[:,2]
#q1=sum*P1
#print(q1)
R =[ 0.8660  ,  0.2500  ,  0.4330, 0  ,  0.8660 ,  -0.5000, -0.5000 ,   0.4330 ,   0.7500]
T = [ -0.4, 0.3 ,0.6]
P2=[R,T]
print(P2)
q = np.dot(P2, Q.T)     #FOR Camera2
q = q.T
u2 = q[:,0]/q[:,2]
v2 = q[:,1]/q[:,2]

q2=P2*Q
print(q2)









