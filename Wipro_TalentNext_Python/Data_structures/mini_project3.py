# mini_project3.py

def calculate_average(student_data, name):
    if name in student_data:
        marks = student_data[name]
        average = sum(marks) / len(marks)
        return average
    else:
        return None

def main():
    # Student data (hardcoded, but can be made dynamic)
    students = {
        "Krishna": [67, 68, 69],
        "Arjun": [70, 98, 63],
        "Malika": [52, 56, 60]
    }

    # Ask user for student name
    name = input("Enter a name: ")

    # Get average
    avg = calculate_average(students, name)

    # Output result
    if avg is not None:
        print(f"Average percentage mark: {int(avg)}")
    else:
        print("Student not found.")

if __name__ == "__main__":
    main()
