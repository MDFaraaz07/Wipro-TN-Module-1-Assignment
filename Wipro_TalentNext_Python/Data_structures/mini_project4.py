# mini_project4.py

def count_name_occurrences(text, name="Alex"):
    return text.count(name)

def main():
    # Input string
    text = input("Enter the string: ")

    # Constraint check
    if 1 <= len(text.split()) <= 200:
        count = count_name_occurrences(text, "Alex")
        print(f"{count}")
    else:
        print("Input does not meet the word count constraint (1 <= n <= 200).")

if __name__ == "__main__":
    main()
