class Solution:
    def mini(arr,start,end):
        ma=arr[0]
        for i in range(start,end):
            if arr[i]<ma:
                ma=arr[i]
        return ma
    def maxi(arr,start,end):
        mx=arr[0]
        for i in range(start,end):
            if arr[i]>mx:
                mx=arr[i]
        return mx
    def is_sorted(arr):
            return arr==sorted(arr)
    def maximumProfit(self, prices):
        profit=0
        n=Solution.mini(prices,0,len(prices))
        m=Solution.maxi(prices,0,len(prices))
        x=len(prices)-1
        if Solution.is_sorted(prices):
            if n==prices[len(prices)-1]:
                return 0
            elif m==prices[len(prices)-1]:
                profit=(prices[x]-prices[0])
        else:
            for i in range(x+1):
                for j in range(0,x+1):
                    if profit<prices[j]-prices[i] and i<j:
                        profit=prices[j]-prices[i]
            
        return profit
sol=Solution()
prices=[23,3,32]
print(sol.maximumProfit(prices))
