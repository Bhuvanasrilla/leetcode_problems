class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=Node('head')
        self.rear=None
    
    def enqueue(self,data):
        new_node=Node(data)
        if self.head.next==None:
            self.head.next=new_node
            self.rear=new_node
            return
        else:
            self.rear.next=new_node
            self.rear=new_node
            return
    
    def dequeue(self):
        if self.head.next==None:
            return "Queue is empty!!"
        temp=self.head.next
        value=temp.data
        self.head.next=temp.next
        temp.next=None
        return value
    
    def peek(self):
        temp=self.head.next
        if temp!=None:
            return temp.data
        else:
            return None
        
    def isEmpty(self):
        if self.head.next==None:
            return True
        else:
            return False
    
    def getFront(self):
        if self.head.next==None:
            return None
        else:
            temp=self.head.next
            return temp.data
        
    def getRear(self):
        if self.rear==None:
            return None
        else:
            return self.rear.data
        

queue=LinkedList()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.peek())
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
print(queue.peek())
queue.dequeue()
queue.dequeue()
print(queue.getFront())
print(queue.getRear())

