#
a = int(input("enter the no"))
print(a)
temp=a
sum=0
while(temp>0):
      d=temp%10
      d=d*d*d
      sum=sum+d
      temp=temp//10

if(sum==a):
      print("amstrong number")
else:
      print("not amstrong number")
