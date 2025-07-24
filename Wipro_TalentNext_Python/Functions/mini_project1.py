# mini_project1.py

def sort_colors(color_sequence):
    """
    Accepts a hyphen-separated color string, sorts the colors alphabetically,
    and returns the sorted hyphen-separated string.
    """
    # Split the input string by hyphen
    color_list = color_sequence.split('-')

    # Sort the list alphabetically
    color_list.sort()

    # Join it back with hyphen and return
    return '-'.join(color_list)


# --- Sample Execution ---
if __name__ == "__main__":
    user_input = input("Enter hyphen-separated color names: ")
    sorted_colors = sort_colors(user_input)
    print("Sorted colors:", sorted_colors)
