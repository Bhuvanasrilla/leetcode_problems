arr=[3,5,0,0,4]
n=len(arr)
for i in range(n-1,-1,-1):
    print(i)
    mini=arr[i]
    for j in range(0,i):
        if arr[j]<mini:
            temp=arr[j]
            arr[j]=arr[i]
            arr[i]=temp
            mini=temp
for i in range(n):
    print(arr[i],end=",")
