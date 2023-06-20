from faker import Faker
import pandas as pd
import random

fake = Faker()



def generate_fake_data(num_rows):
    data = []
    for _ in range(num_rows):
        identity = fake.random_number(digits=6)
        name = fake.name()
        address = fake.address().replace("\n", ", ")
        date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=90).strftime("%m-%d-%Y")
        data.append([identity, name, address, date_of_birth])

    # Add duplicate identities
    duplicates = random.sample(data, int(num_rows * 0.1))  # Assuming 10% duplicates
    for duplicate in duplicates:
        random = random.random()
        if (random < 0.5)


    data += duplicates

    random.shuffle(data)
    return data

# Generate synthetic dataset with 1000 rows
dataset = generate_fake_data(1000)

# Convert list to DataFrame
df = pd.DataFrame(dataset, columns=['ID', 'Name', 'Address', 'Date of Birth'])

# Save DataFrame to CSV
df.to_csv('data/synthetic_dataset.csv', index=False)
