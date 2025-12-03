class Queue:
    def __init__(self,arr,capacity):
        self.arr=arr
        self.capacity=capacity
        self.size=0
        self.front=0
        self.rear=-1

    def enqueue(self,data):
        if self.size==self.capacity:
            return "Overflow!!"
        self.rear=(self.rear+1)%self.capacity
        self.arr[self.rear]=data
        self.size+=1
        return "data is inserted successfully.."
    
    def dequeue(self):
        if self.size==0:
            return "Underflow!!"
        value=self.arr[self.front]
        self.arr[self.front]=-1
        self.front=(self.front+1)%self.capacity
        self.size-=1
        return value
    
    def peek(self):
        if self.size==0:
            return None
        return self.arr[self.front]
    
    def isEmpty(self):
        if self.size==0:
            return True
        else:
            return False
        
    def getRear(self):
        if self.size==0:
            return -1
        else:
            return self.arr[self.rear]
    
    def getFront(self):
        return self.arr[self.front]
    

arr=[-1]*6
circularQueue=Queue(arr,6)
print(circularQueue.enqueue(1))
print(circularQueue.enqueue(2))
print(circularQueue.enqueue(3))
print(circularQueue.peek())
print(circularQueue.arr)
print(circularQueue.enqueue(4))
print(circularQueue.enqueue(5))
print(circularQueue.arr)
print(circularQueue.dequeue())
print(circularQueue.dequeue())
print(circularQueue.arr)
print(circularQueue.peek())
print(circularQueue.getRear())
print(circularQueue.getFront())
print(circularQueue.enqueue(6))
print(circularQueue.arr)
print(circularQueue.peek())
print(circularQueue.getRear())
print(circularQueue.getFront())
print(circularQueue.arr)
print(circularQueue.dequeue())
print(circularQueue.dequeue())
print(circularQueue.arr)
print(circularQueue.enqueue(7))
print(circularQueue.enqueue(8))
print(circularQueue.enqueue(9))
print(circularQueue.arr)