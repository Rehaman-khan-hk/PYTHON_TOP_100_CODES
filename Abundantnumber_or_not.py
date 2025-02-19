num=int(input("Enter the number:"))
sum=1
for i in range(sum,num):
    if(num%i==0):
        sum=sum+i
if(sum>num):
    print(num,"is a Abundant Number")
else:
    print(num,"is Not a Abundant Number")