def prime_check(num):
    n=num
    i=1
    j=num
    count=0
    while i<=j:
        if n%i==0:
            print(i)
            if n/i!=i:
                print(int(n/i))
                count+=2
            else:
                count+=1
        i+=1
        j=n/i
    return count

num=int(input("enter the number"))
print("no of factors of",num,"is",prime_check(num))