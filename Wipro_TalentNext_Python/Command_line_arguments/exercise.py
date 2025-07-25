import sys
import os

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def program1_sum_two_numbers():
    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        print(f"Sum: {num1 + num2}")
    except (IndexError, ValueError):
        print("Please provide two valid integers as arguments.")
    
def program2_welcome_message():
    try:
        message = sys.argv[1]
        print(f"File Name: {os.path.basename(__file__)}")
        print(f"Welcome Message: {message}")
    except IndexError:
        print("Please provide a welcome message as an argument.")

def program3_sum_of_prime_numbers():
    try:
        if len(sys.argv[1:]) != 10:
            print("Please provide exactly 10 numbers.")
            return
        numbers = list(map(int, sys.argv[1:]))
        prime_sum = sum(num for num in numbers if is_prime(num))
        print(f"Sum of prime numbers: {prime_sum}")
    except ValueError:
        print("Please provide valid integers only.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  Program 1 (sum two): python exercise.py 12 8")
        print("  Program 2 (welcome): python exercise.py \"Welcome to Python!\"")
        print("  Program 3 (10 numbers): python exercise.py 2 3 4 5 6 7 8 9 10 11")
    elif len(sys.argv) == 3 and sys.argv[1].isdigit() and sys.argv[2].isdigit():
        program1_sum_two_numbers()
    elif len(sys.argv) == 2:
        program2_welcome_message()
    elif len(sys.argv) == 11:
        program3_sum_of_prime_numbers()
    else:
        print("Invalid number of arguments.")
