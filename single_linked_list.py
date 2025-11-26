class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.length=0
    
    def traverse(self):
        if self.head==None:
            return
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        return temp
        
    def append(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            self.length+=1
            return 
        else:
            temp=self.traverse()
            temp.next=new_node
        self.length+=1
    
    def insert_begining(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            self.length+=1
        else:
            new_node.next=self.head
            head=new_node
            self.length+=1


    def insert(self,data,pos):
        if self.head==None:
            return None
        if pos==0:
            self.insert_begining(data)
            return
        elif pos==self.length+1:
            self.append(data)
            return
        elif 0<pos<=self.length:
            new_node=Node(data)
            temp=self.head
            prev=None
            for i in range(1,pos):
                prev=temp
                temp=temp.next
            prev.next=new_node
            new_node.next=temp
            self.length+=1

    def delete_end(self):
        if self.head==None:
            return None
        elif self.length==1:
            self.head=None
            self.length=0
        else:
            temp=self.head
            prev=None
            while temp.next!=None:
                prev=temp
                temp=temp.next
            prev.next=None
            self.length-=1

    def delete_begin(self):
        if self.head==None:
            return None
        temp=self.head.next
        self.head.next=None
        self.head=temp
        self.length-=1

    def delete_at_pos(self,pos):
        if self.head==None:
            return None
        if pos>=self.length or pos<0:
            print("OUT OF INDEX")
            return None
        if pos==0:
            self.delete_begin()
        elif pos==self.length-1:
            self.delete_end()
        elif 0<pos<=self.length-1:
            temp=self.head
            prev=None
            for i in range(1,pos+1):
                prev=temp
                temp=temp.next
            prev.next=temp.next
            temp.next=None
            self.length-=1
        return

    def search(self,value):
        if self.head==None:
            return None
        temp=self.head
        while temp!=None:
            if temp.data==value:
                return "Found"
            temp=temp.next
        return "Not found"

    def printlist(self):
        if self.head==None:
            return None
        temp=self.head
        while temp!=None:
            print(temp.data,end=' ')
            temp=temp.next
        print()

singlelist=LinkedList()
singlelist.append(10)
singlelist.append(20)
singlelist.append(30)
singlelist.append(40)
singlelist.append(50)
singlelist.insert(25,5)
#singlelist.printlist()
#print(singlelist.length)
#singlelist.delete_at_pos(6)
#print(singlelist.search(10))
