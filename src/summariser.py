import pandas as pd
import os
import re
import google.generativeai as genai

# Load your dataset
df = pd.read_csv('Dataset/Single_Hotel_Dataset.csv')

# Concatenate all reviews into one string
all_reviews = " ".join(df['REVIEWS'].tolist())

# Retrieve the API key from Colab’s secrets
GOOGLE_API_KEY = 'AIzaSyCdU-qCf2UmeF8lmvcH2AYfNgdpQzYgBs8'

# Configure the API key for Google Generative AI
genai.configure(api_key=GOOGLE_API_KEY)

# Gemini 1.5 Flash

# Initialize the GenerativeModel with the Gemini summarization model
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Define the list of aspects you want to focus on

#aspects = ["Location", "Parking", "Cleanliness", "Transportation", "Internet", "Restaurant"]

aspects = []

# Create the prompt based on whether aspects are provided
if aspects:
    prompt = f"Provide a summary of the hotel reviews, focusing just on the following aspects: {', '.join(aspects)} in short."
else:
    prompt = "Provide an overall pointwise summary of the hotel reviews, focusing on key strengths and weaknesses in short"

# Generate the summary for all reviews
response = model.generate_content([prompt, all_reviews])

# Remove `**` (bold formatting) and `##` (heading formatting) from the summary
cleaned_text = re.sub(r'\*\*', '', response.text)
cleaned_output = re.sub(r'## ', '', cleaned_text)

# Print the summarized text
print(cleaned_output)