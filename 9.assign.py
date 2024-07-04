a= input(" enter the  mail :")
i=0
at=0
an=0
l=0
n=0
u=0
if a.endswith(".com") or a.endswith(".in"):
    if(a.count("@")==1):
        for i in a:
            if i.isalnum():
                if i.isalpha():
                    if i.islower():
                        l=l+1
                    else :
                        if i.isupper():
                            u=u+1
                else:
                    if i.isnumeric()or i.isdigit():
                        n=n+1
                        
            else:
                    if i=="@":
                        
                        at=at+1
            

if (l>=1)and(n>=1)and(at==1)and(u==0):
    print("valid mail")
else:
    print("invalid")
