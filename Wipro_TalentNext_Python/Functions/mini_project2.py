# mini_project2.py

from string_utils import ispalindrome, count_the_vowels, frequency_of_letters

# Accept input from user
name = input("Enter the name: ")

# Palindrome check
if ispalindrome(name):
    print("Yes it is a palindrome.")
else:
    print("No it is not a palindrome.")

# Count vowels
vowel_count = count_the_vowels(name)
print(f"No of vowels: {vowel_count}")

# Frequency of letters
freq = frequency_of_letters(name)
print("Frequency of letters:")
for char, count in sorted(freq.items()):
    print(f"{char}-{count}", end=", ")
