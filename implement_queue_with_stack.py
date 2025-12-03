class MyQueue:

    def __init__(self):
        self.arr=[]
        self.top=-1

    def push(self, x: int) -> None:
        self.arr.append(x)
        self.top=len(self.arr)-1

    def pop(self) -> int:
        if self.arr==[]:
            return -1
        self.top=0
        val=self.arr[self.top]
        if len(self.arr)==1:
            del self.arr[self.top]
            self.top=-1
        else:
            del self.arr[self.top]
        self.top=len(self.arr)-1
        return val
        

    def peek(self) -> int:
        if self.top==-1:
            return -1
        return self.arr[0]
        
    def empty(self) -> bool:
        if self.top==-1:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()