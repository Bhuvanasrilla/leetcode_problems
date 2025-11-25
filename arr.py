class Solution:
    def maxi(arr):
        maxi=arr[0]
        for i in range(len(arr)):
            if arr[i]>maxi: 
                maxi=arr[i]
        return maxi
    def pos(arr):
        s=0
        for i in range(len(arr)):
            if arr[i]<0:
                s-=1
        if s==(len(arr)-2*len(arr)):
            return 1
        else:
            return 0
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr):
        maxi=Solution.maxi(arr)
        print("max:",maxi)
        if Solution.pos(arr)==1:
            return 1
        else:
            for i in range(0,len(arr)):
                if arr[i]+1 not in arr and arr[i]>=0:
                    return arr[i]+1
                else:
                    return maxi+1

