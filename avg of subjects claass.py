a=int(input ("sub1"))

b=int(input ("sub2"))
c=int(input ("sub3"))

d=int(input ("sub4"))

e=int(input ("sub5"))

sum=a+b+c+d+e
print(sum)
avg=sum/5
print(avg)
if(avg>90 and avg<=100):
    print("grade is A+")
elif(avg>80 and avg<=90):
    print("grade is A")
elif(avg>70 and avg<=80):
    print("grade is B+")
elif(avg>60 and avg<=70):
    print("grade is B")
elif(avg>50 and avg<=60):
    print("grade is C")
else:
    print(" FAIL")
print("tamil",a)
print("english",b)
print("science",c)
print("maths",d)
print("python",e)
print("total",sum)
print("average",avg)
print("grade",end="")
