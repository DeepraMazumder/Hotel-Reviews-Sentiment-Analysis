import csv  # Importing the CSV module to handle CSV file operations
from scraper import review_scraper  # Importing the custom review scraper function

# List of hotel names to scrape reviews for
hotels = [
    "The Alexandrian Old Town Alexandria, Autograph Collection"
]

# Initialize an empty list to store the collected reviews
dataset = []

# Loop through each hotel in the list
for hotel in hotels:
    try:
        # Call the review_scraper function to scrape reviews for the current hotel
        result = review_scraper(hotel)
        
        # Check if the result is not None or empty
        if result:
            # If valid reviews are returned, add them to the dataset
            dataset.extend(result)
        else:
            # If no reviews are found or an error occurred during scraping
            print(f"No reviews found for {hotel} or an error occurred.")
    
    except Exception as e:
        # Specific error handling for known issues
        if "disconnected: not connected to DevTools" in str(e):
            # Handle connection issues specifically and skip the current hotel
            print(f"Skipping {hotel} due to connection issues.")
        else:
            # Handle any other exceptions and provide error details
            print(f"An error occurred while processing {hotel}: {e}")
        
        # Continue to the next hotel in case of an error
        continue

# Print the total number of reviews collected
print(f"Total reviews collected: {len(dataset)}")

# If the dataset is not empty, print the first review as a sample
if dataset:
    print(f"First review: {dataset[0]}")
    print("-" * 10)  # Print a separator line for clarity

# Write the collected reviews to a CSV file
with open('Custom.csv', mode='w', newline='', encoding='utf-8') as file:
    # Create a CSV writer with the dictionary keys as fieldnames
    writer = csv.DictWriter(file, fieldnames=['REVIEWS'])
    
    # Write the header (column names) to the CSV file
    writer.writeheader()
    
    # Write each review in the dataset as a row in the CSV file
    for row in dataset:
        writer.writerow(row)

# Print a confirmation message after the CSV file is successfully created
print("CSV file created successfully.")