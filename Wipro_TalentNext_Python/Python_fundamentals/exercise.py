# Q1: Check if a number is Positive, Negative, or Zero
num = float(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

# Q2: Check if a number is Odd or Even
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Q3: Check if two numbers have the same last digit
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a % 10 == b % 10:
    print("True - Same last digit")
else:
    print("False - Different last digits")

# Q4: Print numbers from 1 to 10 in a single row with tab space
for i in range(1, 11):
    print(i, end="\t")
print()  # for new line

# Q5: Print even numbers between 23 and 57 (each in a new line)
for i in range(23, 58):
    if i % 2 == 0:
        print(i)

# Q6: Check if a number is Prime
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
else:
    print("Not a prime number")

# Q7: Print prime numbers between 10 and 99
print("Prime numbers between 10 and 99:")
for num in range(10, 100):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)

# Q8: Sum of all digits of a given number
num = int(input("Enter a number: "))
total = 0
n = num
while n > 0:
    total += n % 10
    n //= 10
print("Sum of digits:", total)

# Q9: Reverse a given number
num = int(input("Enter a number: "))
reverse = 0
n = num
while n > 0:
    reverse = reverse * 10 + n % 10
    n //= 10
print("Reversed number:", reverse)

# Q10: Check if a number is a Palindrome
num = int(input("Enter a number: "))
original = num
reverse = 0
while num > 0:
    reverse = reverse * 10 + num % 10
    num //= 10
if original == reverse:
    print(f"{original} is a palindrome.")
else:
    print(f"{original} is not a palindrome.")
