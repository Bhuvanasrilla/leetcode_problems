class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=Node('head')

    def push(self,data):
        new_node=Node(data)
        if self.head.next==None:
            self.head.next=new_node
            return
        if self.head.next!=None:
            new_node.next=self.head.next
            self.head.next=new_node
    
    def pop(self):
        if self.head.next==None:
            return "stack is empty!!"
        temp=self.head.next
        if temp.next==None:
            value=temp.data
            self.head.next=None
            return value
        else:
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


stack=LinkedList()
print(stack.peek())
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek())
print(stack.pop())
print(stack.pop())
print(stack.peek())


