number = int(input("Enter number three digit:") )
first_digit = number // 100
last_digit= number % 10
print(("First number: "), first_digit)
print(("Last number: "), last_digit)
if first_digit == last_digit:
    print("The number is a palindrom")
else:
    print("The number is not a palindrom ")
