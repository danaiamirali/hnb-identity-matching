import random
from faker import Faker
import pandas as pd
from typing import List

fake = Faker()


def generate_fake_data(num_rows):
    data = []
    for _ in range(num_rows):
        identity = fake.random_number(digits=6)
        name = fake.name()
        address = fake.address().replace("\n", ", ")
        date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=90).strftime("%m-%d-%Y")
        email = fake.email()
        data.append([identity, name, address, date_of_birth, email])

    random.shuffle(data)
    return data


if __name__ == "__main__":
    # Generate synthetic dataset with 1000 rows
    dataset = generate_fake_data(1000)

    # Convert list to DataFrame
    df = pd.DataFrame(dataset, columns=['ID', 'Name', 'Address', 'Date of Birth'])

    # Save DataFrame to CSV
    df.to_csv('data/synthetic_dataset.csv', index=False)
