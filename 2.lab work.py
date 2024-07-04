a=int(input("enter the value"))
li=[]
for i in range (a):
    li.append(int(input("enter the valiye")))
se=int(input("enter the number"))
flag=False
for i in range(0,len(li)):
    if li[i]==se:
        print(i)
        break

        
    
