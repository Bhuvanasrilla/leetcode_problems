class Solution:
    def rotateArr(self, arr, d):
        n=len(arr)-1
        temp=[0]*len(arr)
        if d<len(arr):
            x=d//n
            d=d-(x*n)
        for i in range(0,d):
            temp[len(arr)-d+i]=arr[i]
        for i in range(n,d-1,-1):
            temp[i-d]=arr[i]
        arr=temp
        return arr
sol=Solution()
arr=[7,3,9,1]
print(sol.rotateArr(arr,3))
