import pandas as pd
import re
import google.generativeai as genai
from dotenv import load_dotenv
import os

class Summariser:
    def __init__(self):
        load_dotenv()
        self.google_api_key = os.getenv('GOOGLE_API_KEY')
    
    def summarize_reviews(self, data, aspects=None):

        # Concatenate all reviews into one string
        all_reviews = " ".join(data['REVIEWS'].tolist())

        # Configure the API key for Google Generative AI
        genai.configure(api_key=self.google_api_key)

        # Initialize the GenerativeModel with the Gemini summarization model
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")

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

        return cleaned_output