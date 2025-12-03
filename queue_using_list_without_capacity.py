class Queue:
    def __init__(self,arr):
        self.arr=arr
        self.rear=-1

    def enqueue(self,data):
        self.arr.append(data)
        self.rear=data
        return "element is inserted.."

    def dequeue(self):
        if self.rear==-1:
            return "queue is empty.."
        else:
            value=self.arr[0]
            del self.arr[0]
            return value
    
    def peek(self):
        return self.rear

    def isEmpty(self):
        if self.rear==-1:
            return True
        else:
            return False

arr=[]
queue=Queue(arr)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.peek())
queue.enqueue(4)
queue.enqueue(5)
print(queue.peek())
print(queue.dequeue())
print(queue.dequeue())
print(queue.peek())
print(queue.isEmpty())

        
