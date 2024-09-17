#Solution 3: Set Operations and Dictionary Creation

import json

def set_operations_with_dictionary():
    # Step 1: Input a list of student names
    student_names = input("Enter student names (separated by spaces): ").split()

    # Step 2: Convert the list to a set to remove duplicates
    student_set = set(student_names)
    print(f"Set (no duplicates): {student_set}")

    # Step 3: Convert the set to a frozenset
    student_frozenset = frozenset(student_set)
    print(f"Frozenset: {student_frozenset}")

    # Step 4: Create a dictionary with names and their lengths
    name_length_dict = {name: len(name) for name in student_frozenset}
    print(f"Dictionary of name lengths: {name_length_dict}")
    # Step 5: Write the dictionary to a JSON file
    with open('student_names.json', 'w') as file:
        json.dump(name_length_dict, file)
    print("Dictionary written to JSON file.")

    # Step 6: Read from the JSON file and display the contents
    print("Reading from JSON file...")
    with open('student_names.json', 'r') as file:
        data = json.load(file)
        print(data)

set_operations_with_dictionary()


