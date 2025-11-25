class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def forward_traverse(self):
        if self.head==None:
            return None
        temp=self.head
        while temp!=None:
            print(temp.data,end=' ')
            temp=temp.next
        print()
    
    def backward_traverse(self):
        if self.head==None:
            return None
        temp=self.tail
        while temp!=None:
            print(temp.data,end=' ')
            temp=temp.prev
        print()

    def insert_begin(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            self.tail=new_node
        else:
            temp=self.head
            new_node.next=temp
            temp.prev=new_node
            self.head=new_node
        self.length+=1
    
    def append(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            self.tail=new_node
        else:
            temp=self.tail
            temp.next=new_node
            new_node.prev=temp
            self.tail=new_node
        self.length+=1

    def delete_begin(self):
        if self.head==None:
            return None
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            temp=self.head
            self.head=temp.next
            temp.next.prev=None
            temp.next=None
        self.length-=1


doublelinkedlist=LinkedList()
doublelinkedlist.insert_begin(10)
doublelinkedlist.append(20)
doublelinkedlist.append(30)
doublelinkedlist.append(40)
doublelinkedlist.append(50)
doublelinkedlist.forward_traverse()
print(doublelinkedlist.tail.data)
print(doublelinkedlist.head.data)
print(doublelinkedlist.length)
doublelinkedlist.delete_begin()
doublelinkedlist.forward_traverse()
print(doublelinkedlist.tail.data)
print(doublelinkedlist.head.data)
print(doublelinkedlist.length)

