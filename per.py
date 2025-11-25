class Solution:
    def reverse(arr,start,end):
        while(start<end):
            arr[start],arr[end]=arr[end],arr[start]
            start+=1
            end-=1
    def nextPermutation(self, arr):
        pivot=0
        k=0
        for i in range(len(arr)-1,0,-1):
            if arr[i]>arr[i-1]:
                pivot=arr[i-1]
                k=i-1
                break
        if pivot==0:
            Solution.reverse(arr,0,len(arr)-1)
        else:
            for i in range(len(arr)-1,-1,-1):
                if arr[i]>pivot:
                    arr[i],arr[k]=arr[k],arr[i]
                    break
            Solution.reverse(arr,k+1,len(arr)-1)
        return arr
sol=Solution()
arr=[1,2,3,6,5,4]
print(sol.nextPermutation(arr))
print(11//3)

