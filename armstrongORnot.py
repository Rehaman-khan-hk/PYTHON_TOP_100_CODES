number=370
num=number
digit=0
sum=0
length=len(str(num))
for i in range (length):
    digit=int(num%10)
    num=num/10
    sum=sum+pow(digit,length)
if sum==number:
    print("ARMSTRONG NUMBER")
else:
    print("NOT AN ARMSTRONG NUMBER")