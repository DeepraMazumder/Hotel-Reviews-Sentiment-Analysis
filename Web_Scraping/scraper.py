from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def review_scraper(hotel_name="itc"):
    REVIEW_LIST = []
    collected_reviews = set()
    service_obj = Service("./chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)

    try:
        driver.get("https://www.google.com/travel")
        sleep(2)  # Wait for page to load
        
        # Locate and interact with search input
        driver.find_element(By.XPATH, "//input[@type='text']").send_keys(hotel_name + Keys.RETURN)
        sleep(2)

        # Click on the first search result
        text_input = driver.find_elements(By.CSS_SELECTOR, "li[class = 'Q1RWxd']")
        if text_input:
            first_element = text_input[0]
            first_element.click()
            sleep(2)
            
            # Click on the Reviews tab
            try:
                rev_tab = driver.find_element(By.XPATH, "//span[text()='Reviews']")
                rev_tab.click()
                sleep(2)
            except Exception as e:
                print(f"Failed to find or click Reviews tab: {e}")
                return None
            
            # Loop to handle pagination
            while True:
                review_elements = driver.find_elements(By.XPATH, "//div[contains(@class, 'review')]")
                for review_element in review_elements:
                    review_texts = review_element.find_elements(By.XPATH, ".//span[@class='review-text']")
                    for review_text in review_texts:
                        review_content = review_text.text.strip()
                        if review_content and review_content not in collected_reviews:
                            REVIEW_LIST.append({"review": review_content})
                            collected_reviews.add(review_content)
                
                # Scroll down to load more reviews if necessary
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(2)  # Allow time for reviews to load

                # Check for next page button
                try:
                    next_button = driver.find_element(By.XPATH, "//span[text()='Next']")
                    if next_button.is_displayed():
                        next_button.click()
                        sleep(3)  # Adjust sleep time if needed
                    else:
                        break  # No more pages
                except Exception as e:
                    print(f"No more pages or an error occurred: {e}")
                    break

        else:
            print("No elements found with the given selector.")
            return None

    finally:
        driver.close()
        return REVIEW_LIST