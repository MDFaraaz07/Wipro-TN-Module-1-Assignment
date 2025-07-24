# mini_project.py

import re
from collections import Counter

def get_meeting_time(line_count):
    # Convert line count to 12-hour format and determine AM/PM
    if line_count <= 12:
        return f"{line_count} AM"
    else:
        hour = line_count - 12
        return f"{hour} PM"

def get_meeting_place(text):
    # Normalize words: remove punctuation, convert to lowercase
    words = re.findall(r'\b\w+\b', text.lower())

    # Count word frequencies
    word_counts = Counter(words)

    # Get the most common word
    most_common_word, _ = word_counts.most_common(1)[0]

    # Capitalize the first letter for proper formatting
    return f"{most_common_word.capitalize()} Street"

def main():
    # Path to the input file
    file_path = "Sample.txt"  # Make sure Sample.txt is in the same directory or provide full path

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            text = file.read()  # This will be empty since we already read lines

        # If we need entire text, read from joined lines instead
        full_text = ' '.join(lines)

        # Get number of lines
        num_lines = len(lines)

        # Get time and place
        meeting_time = get_meeting_time(num_lines)
        meeting_place = get_meeting_place(full_text)

        # Output the result
        print(f"Meeting time: {meeting_time}")
        print(f"Meeting place: {meeting_place}")

    except FileNotFoundError:
        print(f"File '{file_path}' not found. Please check the path and try again.")

if __name__ == "__main__":
    main()
