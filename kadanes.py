class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def total(arr,start,end):
        tot=0
        for i in range(start,end+1):
            tot+=arr[i]
        return tot
    def pos(arr):
        s=0
        for i in range(len(arr)):
            if arr[i]>=0:
                s+=1
        if s==len(arr):
            return True
        else:
            return False
    def maxSubArraySum(self,arr):
        sum1=0
        temp=0
        tot1=0
        tot2=0
        temp3=0
        tot=0
        s=-1
        if Solution.pos(arr):
            tot=Solution.total(arr,0,len(arr)-1)
        else:
            for i in range(len(arr)):
                if arr[i]<0:
                    temp=Solution.total(arr,0,len(arr)-1)
                    print("temp:",temp)
                    temp1=Solution.total(arr,0,i)
                    print("temp1:",temp1)
                    temp2=Solution.total(arr,i+1,len(arr)-1)
                    print("temp2:",temp2)
                    sum1=max(temp1,temp2)
                    print("sum1:",sum1)
                    if tot1<max(temp,sum1) and temp>0 and sum1>0:
                        tot1=max(temp,sum1)
                        print("tot1:",tot1)
                    elif tot1>max(temp,sum1) and temp<=0 and sum1<=0:
                        tot1=max(temp,sum1)
                        print("tot1:",tot1)
                elif arr[i]>=0:
                    if (i==0 or i==s+1) or (s==0 and i-1==0 and i>0):
                        temp3=arr[i]
                        if i==0:
                            tot2+=temp3
                            s=i
                        else:
                            s=i
                            tot2+=temp3
                        print("tot2:",tot2)
                    elif s!=-1:
                        tot2=0
                        temp3=arr[i]
                        tot2+=temp3
                        s=i
                        print("tot2:",tot2)
                        
                        
            if (tot1==0 and tot2==0) or(tot1!=0 and tot2!=0):       
                tot=max(tot1,tot2)
            elif (tot1==0 and tot2<0) or (tot1<0 and tot2==0):
                tot=min(tot1,tot2)
                    
            
                
        return tot
sol=Solution()
arr=[51,-41,67,-48,7,-67,-97,22,50,-71]
print(sol.maxSubArraySum(arr))
