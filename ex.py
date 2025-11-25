class Solution:
    def reverseArray(self, arr):
        temp=[0]*len(arr)
        for i in range(len(arr)-1,-1,-1):
            print(len(arr)-i-1)
            print(temp)
            temp[len(arr)-i-1]=arr[i]
        arr=temp
        return arr
sol=Solution()
arr=[1,4,3,2,6,5]
print(sol.reverseArray(arr))

print(arr)
print(4//2)
