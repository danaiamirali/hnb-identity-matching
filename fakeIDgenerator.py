import pandas as pd
from faker import Faker

# Initialize Faker object
fake = Faker()

# Generate data
data = []
for i in range(3500):
    first_name = fake.first_name()
    last_name = fake.last_name()
    address = fake.address().replace("\n", ", ")
    date = fake.date_between(start_date='-30y', end_date='-20y')
    id = i + 11111111
    data.append([id, first_name, last_name, address, date])

# Create DataFrame
df = pd.DataFrame(data, columns=['ID', 'First Name', 'Last Name', 'Address', 'Date'])

df.to_csv('random_data.csv', index=False)