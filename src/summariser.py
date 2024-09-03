import os
import re

import google.generativeai as genai
from dotenv import load_dotenv

report_template = """
**Introduction:**
Provide an overview of the hotel, including its name and location, based only on the information available in the provided reviews. If no specific details are mentioned, state that no detailed overview is provided in the reviews.

**Summary of Reviews:**
Summarize the overall sentiment of the reviews (e.g., positive, negative, mixed) strictly based on the provided reviews. Mention the average rating if it is explicitly mentioned in the reviews.

**Detailed Review Analysis:**

1. **Cleanliness:**
   - Summarize guest feedback on the cleanliness of the hotel rooms, bathrooms, common areas, etc., strictly using the details from the reviews.
   - Only highlight recurring positive or negative comments if they are mentioned multiple times in the reviews.

2. **Service Quality:**
   - Discuss the staff's hospitality, efficiency, and professionalism based solely on guest reviews.
   - Provide specific examples of service experiences only if explicitly described in the reviews.

3. **Comfort and Amenities:**
   - Review guest opinions on the comfort of the rooms, including bed quality, room size, and noise levels, only using details mentioned in the reviews.
   - Mention feedback on hotel amenities like the pool, gym, spa, restaurant, etc., only if these amenities are explicitly discussed in the reviews.

4. **Location:**
   - Summarize guest opinions on the hotel’s location, including proximity to attractions, transportation, and convenience, strictly based on the reviews.
   - If specific advantages or disadvantages of the location are not mentioned in the reviews, state that there are no details available.

5. **Value for Money:**
   - Analyze how guests perceive the hotel’s value for money based solely on the provided reviews.
   - Only include comments about the price being justified or not if explicitly mentioned by guests.

**Common Praise and Complaints:**
- List the most frequently mentioned positive aspects of the hotel, strictly based on recurring themes in the reviews.
- List the most common complaints or areas of concern, based only on the recurring themes in the reviews.

**Recommendations:**
- Provide suggestions for improvements based only on specific feedback provided in the reviews.
- Highlight strengths to focus on, strictly using guest feedback.

**Conclusion:**
- Conclude with a final assessment of the hotel based strictly on the reviews provided.
- Provide a general recommendation for potential guests considering a stay at the hotel, relying only on the information in the reviews.
"""



class Summariser:
    def __init__(self):
        load_dotenv()
        self.google_api_key = os.getenv('GOOGLE_API_KEY')
      #   self.google_api_key = "AIzaSyADXSFeYLZaf3y4Xaj8RsVSF-9NEEqAsjk"
    
    def summarize_reviews(self, data, aspects=None):
        print(len(data))
        #data = data.sample(400)
        # Concatenate all reviews into one string
        all_reviews = " ".join(data['REVIEWS'].tolist())

        # Configure the API key for Google Generative AI
        genai.configure(api_key=self.google_api_key)

        # Initialize the GenerativeModel with the Gemini summarization model
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")

        # Create the prompt based on whether aspects are provided
        if aspects:
            prompt = f"Provide a detailed summary of the hotel reviews, focusing just on the following aspects: {', '.join(aspects)}. Do not add extra aspects, the summary must strictly be based on the provided reviews. Also mention if proper information is not available regarding any {', '.join(aspects)}."
        else:
            prompt = report_template

        # Generate the summary for all reviews
        response = model.generate_content([prompt, all_reviews])

        # Remove `**` (bold formatting) and `##` (heading formatting) from the summary
        cleaned_text = re.sub(r'\*\*', '', response.text)
        cleaned_output = re.sub(r'## ', '', cleaned_text)
        
        return cleaned_output