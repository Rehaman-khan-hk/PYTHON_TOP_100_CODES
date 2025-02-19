num1=int(input("Enter the first Number:"))
num2=int(input("Enter the second Number:"))
sum1=0
sum2=0
for i in range (1,num1):
    if(num1%i==0):
        sum1=sum1+i
for i in range (1,num2):
    if(num2%i==0):
        sum1=sum2+i
if(sum1==num1 and sum2==num2):
    print("The entered Numbers are friendly pair")
else:
    print("The entered Numbers are friendly pair")