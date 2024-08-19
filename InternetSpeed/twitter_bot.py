from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PROMISED_UP = 10
PROMISED_DOWN = 150
TWITTER_EMAIL = 'jawadaliamjad1113@gmail.com'
TWITTER_PASSWORD = 'jawadali7898'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)



class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        go_button = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a'))
        )
        go_button.click()
        time.sleep(10)
        small_go_button = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a'))
        )
        download = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        upload = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(f'Download: {download}\nUpload: {upload}')
        self.up = upload
        self.down = download
        self.driver.quit()

    def tweet_at_provider(self):
        self.driver.get('https://x.com/home')
