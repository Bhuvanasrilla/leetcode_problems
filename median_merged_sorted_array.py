
def findMedianSortedArrays( nums1, nums2) -> float:
    n1=len(nums1)
    n2=len(nums2)
    i=0
    j=0
    k=0
    res=[0]*(n1+n2)
    median=0
    while i<n1 and j<n2:
        if nums1[i]<=nums2[j]:
            res[k]=nums1[i]
            i+=1
        else:
            res[k]=nums2[j]
            j+=1
        k+=1
    
    while i<n1:
        res[k]=nums1[i]
        k+=1
        i+=1
    while j<n2:
        res[k]=nums2[j]
        k+=1
        j+=1

    n3=n1+n2
    if (n3)%2==0:
        val=res[n3//2]
        print(val)
        val1=res[(n3)//2-1]
        print(val1)
        median=(val1+val)/2
    else:
        val=(n3)//2
        median=res[val]
    return median
    
num1=[0,0]
num2=[3,4]
print(findMedianSortedArrays(num1,num2))
        
    