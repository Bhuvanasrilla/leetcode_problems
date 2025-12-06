import numpy as np

def Relu(val):
    return np.maximum(0,val)
    
def sigmoid(val):
    return 1/(1+np.exp(-val))
    
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])  

w1=np.random.randn(2,2)
w2=np.random.randn(2,1)

b1=np.zeros((1,2))
b2=np.zeros((1,1))

#forward pass
z1= X@w1 + b1
A1=Relu(z1)

print(z1)
print(A1)

z2= z1@w2 + b2
A2=sigmoid(z2)



