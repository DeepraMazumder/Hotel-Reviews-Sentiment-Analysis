from time import sleep
from typing import List

from fastapi import FastAPI, HTTPException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

app = FastAPI()  # Create FastAPI app

# Function to scrape reviews from Google for a given hotel name
def review_scraper(hotel_name: str = "itc") -> List[dict]:
    REVIEW_LIST = []  # List to store collected reviews
    collected_reviews = set()  # Set to keep track of unique reviews
    service_obj = Service("./chromedriver.exe")  # Specify the path to the ChromeDriver executable
    driver = webdriver.Chrome(service=service_obj)  # Initialize the Chrome WebDriver

    # Open Google Travel in the browser
    driver.get("https://www.google.com/travel")
    sleep(2)
    
    # Locate the search input field and enter the hotel name, followed by pressing RETURN
    driver.find_element(By.XPATH, "//input[@type='text']").send_keys(hotel_name + Keys.RETURN)
    sleep(2)

    # Find the first search result that matches the hotel name and click it
    text_input = driver.find_elements(By.CSS_SELECTOR, "li[class = 'Q1RWxd']")
    if text_input:
        first_element = text_input[0]
        first_element.click()
        sleep(2)
        
        # Click on the 'Reviews' tab
        rev_tab = driver.find_element(By.XPATH, "//span[text()='Reviews']")
        rev_tab.click()
        sleep(2)

        # Loop to handle pagination and collect reviews
        while True:
            review_elements = driver.find_elements(By.XPATH, "//div[contains(@class, 'review')]")
            for review_element in review_elements:
                review_texts = review_element.find_elements(By.XPATH, ".//span[@class='review-text']")
                for review_text in review_texts:
                    review_content = review_text.text.strip()
                    if review_content and review_content not in collected_reviews:
                        REVIEW_LIST.append({"review": review_content})
                        collected_reviews.add(review_content)

            # Scroll down to load more reviews if available
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(2)

            # Check for the presence of a 'Next' button to navigate to the next page of reviews
            next_button = driver.find_element(By.XPATH, "//span[text()='Next']")
            if next_button.is_displayed():
                next_button.click()
                sleep(3)
            else:
                break

    else:
        print("No elements found with the given selector.")
        return []

    driver.close()
    
    return REVIEW_LIST

# FastAPI endpoint to get reviews
# 
review_scraper()