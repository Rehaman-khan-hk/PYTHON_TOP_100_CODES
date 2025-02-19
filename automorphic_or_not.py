num=int(input("Enter the Number:"))
square=(pow(num,2))

mod = pow(10, len(str(num)))
if square%mod==num:
    print(num,"is Automorphic number")
else:
    print(num,"is not an Automorphic number")