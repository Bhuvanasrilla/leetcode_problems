import numpy as np

arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr1.shape)
arr2=np.array([[9,8,7],[6,5,4],[3,2,1]])
print(arr2.shape)

result=np.matmul(arr1,arr2)
print(result)

##Implement a simple preceptron prediction.
#f(x)=h(w.x+b)
input=np.array([-6,7,-8,9,10])
w=np.arange(1,6)
b=0.3
print(input.shape)
print(w.shape)
y=np.dot(w,input)+b
print(y)

x = np.array([1, 0, 1])
w = np.array([0.2, -0.5, 0.3])
b = 0.1

y = np.dot(x, w) + b
print(y)