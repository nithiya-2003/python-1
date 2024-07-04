a=input("enter a password")
if ( a.islower()=="false"or"FALSE"  and (a.isupper()=="false"or"FALSE")):
    if (a.isalnum()=="false"or"FALSE")and (("@" in a)or("#" in a)or("."in a) or("&"in a)or("*"in a)):
            if(len(a)>=8):
                print("valid and strong")
            else:
                print("valid but not strong")
    else:
        print(" does not contain any special character invalid")

else:
    print("# contain only lower  AND  upper #so invalid")
        
