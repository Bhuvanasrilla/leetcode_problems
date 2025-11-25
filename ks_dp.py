def knap_sack(w,wt,val,n):
    if n==0 or w==0:
        return 0
    if wt[n-1]>w:
        return knap_sack(w,wt,val,n-1)
    else:
        return max(val[n-1]+knap_sack(w-wt[n-1],wt,val,n-1),knap_sack(w,wt,val,n-1))
if __name__=="__main__":
    w=15
    weight=[2,4,6,9]
    val=[10,10,12,18]
    n=len(val)
    print(knap_sack(w,weight,val,n))
