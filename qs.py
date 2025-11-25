def partiton(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<=pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
def quick_sort(arr,low,high):
    if(low<high):
        pi=partiton(arr,low,high)
        quick_sort(arr,low,pi-1)
        quick_sort(arr,pi+1,high)
data=[20,13,17,19,-10]
print("the unsorted array:")
for i in range(len(data)):
    print(data[i],end=" ")
    n=len(data)
quick_sort(data,0,n-1)
print("the sorted array:")
for i in range(len(data)):
    print(data[i],end=" ")
    
