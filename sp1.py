class Solution:
    def get_min(arr,start,end):
        mi=arr[0]
        for i in range(start,end):
            if mi>arr[i]:
                mi=arr[i]
        return mi
    def get_max(arr,start,end):
        ma=arr[0]
        for i in range(start,end):
            if ma<arr[i]:
                ma=arr[i]
        return ma
    def getMinDiff(self, arr,k):
        arr1=sorted(arr)
        diff=0
        for i in range(0,len(arr1)):
            if arr1[i]<=k:
                arr1[i]+=k
            elif arr1[i]>=k:
                ad=arr1[i]+k
                di=arr1[i]-k
                mi=Solution.get_min(arr1,0,i)
                ma=Solution.get_max(arr1,0,i)
                if ad>ma and di<=mi:
                    if ad-mi>ma-di:
                        arr1[i]=di
                    elif ad-mi<ma-di:
                        arr1[i]=ad
                elif ad>ma and di>mi:
                    if ad-mi>di-ma:
                        arr1[i]=di
                    elif ad-mi<di-ma:
                        arr1[i]=ad
        diff=Solution.get_max(arr1,0,len(arr1))-Solution.get_min(arr1,0,len(arr1)
        return diff
        
