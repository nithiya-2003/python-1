def arith_prog(a,d,n):
    t=0
    at=0
    for i in range(n):
        if t<=n:
            at=a+(t-i)*d
            print(at,end=" ")
            a=a+d
            t=t+1
    return(at)        










a=int(input("enter the first element:"))
d=int(input("enter the common difference:"))
n=int(input("enter no of terms u want"))
arith_prog(a,d,n)
