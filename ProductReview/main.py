import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from textblob import TextBlob

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option('detach', True)
# driver = webdriver.Chrome(chrome_options)

# driver.get('https://www.ebay.com/itm/266324247449?_nkw=pc&itmmeta=01J5JTTT4N7BPR5YQJ4188J0N2&hash=item3e02298399:g:kAYAAOSwXNdmK9ns')


# def get_feedbacks():
#     see_feedback_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, '//*[@id="LISTING_FRAME_MODULE"]/div/div[3]/div[2]/div/div[4]/a'))
#     )
#
#     see_feedback_button.click()
#     time.sleep(3)
#
#     all_feedbacks = []
#     for _ in range(5):
#         time.sleep(2)
#         feedbacks = [feedback.text for feedback in driver.find_elements(By.CLASS_NAME, 'fdbk-container__details__comment')]
#         all_feedbacks.extend(feedbacks)
#         next_button = driver.find_element(By.CLASS_NAME, 'pagination__next')
#         next_button.click()
#     return all_feedbacks


with open('feedbacks', 'r', encoding='utf-8') as file:
    content = file.readlines()

sentiments = []
for feedback in content:
    blob = TextBlob(feedback)
    feedback_score = blob.sentiment.polarity
    print(f'Feedback:{feedback}\nScore:{feedback_score}')


