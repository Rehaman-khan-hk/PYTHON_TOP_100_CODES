n=int(input("Enter the number: "))
temp=n
sum=0
fact=1
while n>0:
    digit=n%10
    fact =1
    print("Digits: ",digit)
    for i in range(1,digit+1):
     fact=fact*i
    print("Factorial of Digit: ", fact)
    sum=sum+fact
    print("Sum",sum)
    n=n//10
if sum==temp:
    print(temp,"The entered number is Strong Number:")
else:
    print(temp,"The entered number is Strong Number:")

   
