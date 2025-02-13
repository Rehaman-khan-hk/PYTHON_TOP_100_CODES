try:
    num = int(input("Enter a Number: "))
    if num % 2 == 0:
        print("Given number is Even")
    else:
        print("Given number is Odd")
except ValueError:
    print("Invalid input! Please enter an integer.")
except KeyboardInterrupt:
    print("\nInput interrupted by user.")
