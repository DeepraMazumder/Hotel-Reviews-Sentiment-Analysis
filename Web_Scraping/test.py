import csv
from scraper import review_scraper

hotels = [
    "The Alexandrian Old Town Alexandria, Autograph Collection"
]

dataset = []
for hotel in hotels:
    try:
        result = review_scraper(hotel)
        if result:  # Check if result is not None or empty
            dataset.extend(result)
        else:
            print(f"No reviews found for {hotel} or an error occurred.")
    except Exception as e:
        # Specific error handling for known issues
        if "disconnected: not connected to DevTools" in str(e):
            print(f"Skipping {hotel} due to connection issues.")
        else:
            print(f"An error occurred while processing {hotel}: {e}")
        continue  # Skip to the next hotel in case of error

print(f"Total reviews collected: {len(dataset)}")
if dataset:
    print(f"First review: {dataset[0]}")
    print("-" * 10)
    # print(dataset[50])

# Writing the dataset to a CSV file
with open('Custom.csv', mode='w', newline='', encoding='utf-8') as file:
    # Create a CSV writer with the dictionary keys as fieldnames
    writer = csv.DictWriter(file, fieldnames=['review'])
    
    # Write the header
    writer.writeheader()
    
    # Write the rows
    for row in dataset:
        writer.writerow(row)

print("CSV file created successfully.")