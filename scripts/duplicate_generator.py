"""
duplicate_generator.py
----------------------
This script takes an existing csv file and
generates duplicate records in the dataset.
"""

import random

NO_OF_DUPLICATES = 400

"""
Function to simulate unintentional errors across fields in a record
"""
def unintentional_errors(data: list[str]) -> list[str]:
    no_of_fields_to_change = random.randint(1, 4)
    for _ in range(no_of_fields_to_change):
        field_id = random.randint(1, len(data)-1)
        field_data = data[field_id]
        operation = random.randint(0, 2)
        if operation == 0:     # Character Replacemnet
            position = random.randint(0, len(field_data)-1) if len(field_data) > 0 else 0
            new_char = random.choice("0123456789abcdefghijklmnopqrstuvwxyz")
            field_data = field_data[:position] + new_char + field_data[position+1:]
        elif operation == 1:     # Character deletion
            position = random.randint(0, len(field_data)-1) if len(field_data) > 0 else 0
            field_data = field_data[:position] + field_data[position+1:]
        elif operation == 2:     # Character insertion
            position = random.randint(0, len(field_data))
            new_char = random.choice("0123456789abcdefghijklmnopqrstuvwxyz")
            field_data = field_data[:position] + new_char + field_data[position:]
        data[field_id]=field_data
    return data

"""
Function to generate duplicate records in a dataset
"""
def generate_duplicates(data: list[str]) -> list[str]:
    no_of_duplicates = random.randint(NO_OF_DUPLICATES - 10, NO_OF_DUPLICATES + 10)

    print("Generating {} duplicates...".format(no_of_duplicates))

    for _ in range(no_of_duplicates):
        duplicate_id = random.randint(0, len(data)-1)
        old = data[duplicate_id]
        new = unintentional_errors(old.copy())
        data.append(new)
        print("Modified record {} to create duplicate record {}".format(duplicate_id, len(data)-1))

    return data

def main():
    # Load csv
    data = []

    with open('data/so_dataset.csv', 'r') as f:
        data = f.readlines()
        data = [line.strip().split(',') for line in data]
        data = data[1:]     # Remove header

    # Generate duplicates
    data = generate_duplicates(data)

    # Shuffle data
    random.shuffle(data)

    # Export to csv
    with open('data/so_dataset_duplicates.csv', 'w') as f:
        for line in data:
            f.write(','.join(line) + '\n')


if __name__ == "__main__":
    main()