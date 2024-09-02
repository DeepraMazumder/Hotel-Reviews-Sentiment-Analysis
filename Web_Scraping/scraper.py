from time import sleep  # Importing sleep function to add delays in execution
from selenium import webdriver  # Importing Selenium WebDriver to automate browser actions
from selenium.webdriver.chrome.service import Service  # Service to manage WebDriver executable
from selenium.webdriver.common.by import By  # By class to locate elements on the web page
from selenium.webdriver.common.keys import Keys  # Keys class to send keyboard inputs like RETURN

# Function to scrape reviews from Google for a given hotel name
def review_scraper(hotel_name="itc"):
    REVIEW_LIST = []  # List to store collected reviews
    collected_reviews = set()  # Set to keep track of unique reviews
    service_obj = Service("./chromedriver.exe")  # Specifying the path to the ChromeDriver executable
    driver = webdriver.Chrome(service=service_obj)  # Initializing the Chrome WebDriver

    try:
        # Open Google Travel in the browser
        driver.get("https://www.google.com/travel")
        sleep(2)  # Wait for the page to fully load
        
        # Locate the search input field and enter the hotel name, followed by pressing RETURN
        driver.find_element(By.XPATH, "//input[@type='text']").send_keys(hotel_name + Keys.RETURN)
        sleep(2)  # Wait for the search results to load

        # Find the first search result that matches the hotel name and click it
        text_input = driver.find_elements(By.CSS_SELECTOR, "li[class = 'Q1RWxd']")
        if text_input:
            first_element = text_input[0]  # Get the first element in the list
            first_element.click()  # Click on the first search result
            sleep(2)  # Wait for the hotel's page to load
            
            # Attempt to click on the 'Reviews' tab
            try:
                rev_tab = driver.find_element(By.XPATH, "//span[text()='Reviews']")
                rev_tab.click()  # Click on the Reviews tab
                sleep(2)  # Wait for the reviews section to load
            except Exception as e:
                print(f"Failed to find or click Reviews tab: {e}")
                return None  # Exit the function if the Reviews tab is not found
            
            # Loop to handle pagination and collect reviews
            while True:
                # Find all review elements on the page
                review_elements = driver.find_elements(By.XPATH, "//div[contains(@class, 'review')]")
                for review_element in review_elements:
                    # Extract the text of each review
                    review_texts = review_element.find_elements(By.XPATH, ".//span[@class='review-text']")
                    for review_text in review_texts:
                        review_content = review_text.text.strip()  # Clean the review text
                        # Add the review to the list if it's not already collected
                        if review_content and review_content not in collected_reviews:
                            REVIEW_LIST.append({"review": review_content})
                            collected_reviews.add(review_content)
                
                # Scroll down to load more reviews if available
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(2)  # Allow time for new reviews to load

                # Check for the presence of a 'Next' button to navigate to the next page of reviews
                try:
                    next_button = driver.find_element(By.XPATH, "//span[text()='Next']")
                    if next_button.is_displayed():
                        next_button.click()  # Click the 'Next' button
                        sleep(3)  # Wait for the next page to load
                    else:
                        break  # Exit loop if no more pages
                except Exception as e:
                    print(f"No more pages or an error occurred: {e}")
                    break  # Exit loop if an error occurs or no more pages are available

        else:
            # If no search results are found, print an error message and return None
            print("No elements found with the given selector.")
            return None

    finally:
        driver.close()  # Close the browser after scraping is complete
        return REVIEW_LIST  # Return the list of collected reviews