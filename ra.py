
class Solution:
    def reverse(arr,start,end):
        while start<end:
            arr[start],arr[end]=arr[end],arr[start]
            start+=1
            end-=1
    def rotateArr(self, arr, d):
        n=len(arr)
        Solution.reverse(arr,0,d-1)
        Solution.reverse(arr,d,n-1)
        Solution.reverse(arr,0,n-1)
        return arr
sol=Solution()
arr=[2,4,6,8,10,12,14,16,18,20]
print(sol.rotateArr(arr,3))

