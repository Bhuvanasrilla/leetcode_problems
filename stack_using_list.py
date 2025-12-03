class Stack:
    def __init__(self,arr):
        self.arr=arr
        self.top=-1
    
    def push(self,data):
        self.arr.insert(0,data)
        self.top+=1
    
    def pop(self):
        if self.isEmpty():
            print("The stack is empty!!")
            return
        value=self.arr.pop(0)
        self.top-=1
        return value

    def peek(self):
        if self.isEmpty():
            print("The stack is empty!!")
        else:
            print(self.arr[0])

    def delete(self):
        self.arr.clear()
        self.top=-1

    def isEmpty(self):
        if self.top==-1:
            return True
        else:
            return False

arr=[]
stack=Stack(arr)
stack.push(1)
stack.push(2)
stack.peek()
stack.push(3)
stack.push(4)
stack.peek()
stack.push(5)
stack.pop()
stack.pop()
stack.peek()