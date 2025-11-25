class Solution:
    def maximumProfit(self,prices) -> int:
        buy=0
        sell=0
        profit=0
        for i in range(1,len(prices)):
            if prices[i-1]<prices[i] and buy==0:
                buy=prices[i-1]
                print("buy is ",buy)
            if buy!=0:
                if prices[i-1]>prices[i]:
                    sell=prices[i-1]
                    print("sell is ",sell)
                    profit+=(sell-buy)
                    buy=0
                    sell=0
                elif i==len(prices)-1:
                    sell=prices[i]
                    print("sell is",sell)
                    profit+=(sell-buy)
        return profit
sol=Solution()
prices=[4,2,2,2,4]
print(sol.maximumProfit(prices))
