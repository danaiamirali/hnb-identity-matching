import random
from faker import Faker
import pandas as pd
from typing import List

fake = Faker()

def unintentional_errors(data: List[str]) -> List[str]:
    no_of_fields_to_change = random.randint(1, 3)
    for _ in range(no_of_fields_to_change):
        field_id = random.randint(1, len(data)-1)
        field_data = data[field_id]
        operation = random.randint(0, 2)
        if operation == 0:     # Character Replacemnet
            position = random.randint(0, len(field_data)-1)
            new_char = random.choice("0123456789abcdefghijklmnopqrstuvwxyz")
            field_data = field_data[:position] + new_char + field_data[position+1:]
        elif operation == 1:     # Character deletion
            position = random.randint(0, len(field_data)-1)
            field_data = field_data[:position] + field_data[position+1:]
        elif operation == 2:     # Character insertion
            position = random.randint(0, len(field_data))
            new_char = random.choice("0123456789abcdefghijklmnopqrstuvwxyz")
            field_data = field_data[:position] + new_char + field_data[position:]
        data[field_id]=field_data
    return data


def generate_fake_data(num_rows):
    data = []
    for _ in range(num_rows):
        identity = fake.random_number(digits=6)
        name = fake.name()
        address = fake.address().replace("\n", ", ")
        date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=90).strftime("%m-%d-%Y")
        email = fake.email()
        data.append([identity, name, address, date_of_birth, email])

    # Add duplicate identities
    duplicates = random.sample(data, int(num_rows * 0.1))  # Assuming 10% duplicates
    for duplicate in duplicates:
        random = random.random()
        if (random < 0.5):
            """
            TO DO
            """
            
            pass


    data += duplicates

    random.shuffle(data)
    return data


if __name__ == "__main__":
    # Generate synthetic dataset with 1000 rows
    dataset = generate_fake_data(1000)

    # Convert list to DataFrame
    df = pd.DataFrame(dataset, columns=['ID', 'Name', 'Address', 'Date of Birth'])

    # Save DataFrame to CSV
    df.to_csv('data/synthetic_dataset.csv', index=False)
