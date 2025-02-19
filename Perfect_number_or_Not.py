n=int(input("Enter the Number: "))
sum=0
for i in range(1,n):
    if n%i==029:
        sum=sum+i
if sum==n:
    print(n,"The entered number is perfect Number")
else:
    print(n,"The entered number is not a  perfect Number")