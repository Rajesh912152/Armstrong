#Armstrong Number (153)
num=int(input())
temp=num
sum=0
length=len(str(num))
while (temp!=0):
    a=temp%10
    sum+=a**length
    temp=temp//10
if (sum==num):
    print("Armstrong")
else:
    print("Not Armstrong")