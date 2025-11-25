class Solution:
    def max(self,arr):
        tot=0
        temp=1
        for i in range(0,len(arr)):
            temp=arr[i]
            for j in range(i+1,len(arr)):
                if j>i:
                    temp*=(arr[j])
                    if tot<temp:
                        tot=temp
        return tot
sol=Solution()
arr=[-2,6,-3,-10,0,2]
print(sol.max(arr)) 
