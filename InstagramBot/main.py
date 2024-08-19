import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

USER_NAME = 'jawadaliamjad1113'
PASS_WORD = 'amjad1133'
SIMILAR_ACCOUNT = 'chefsteps'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(chrome_options)


def log_in():
    driver.get('https://www.instagram.com/')

    user_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input'))
    )
    password = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
    sing_in_button = driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[3]')
    user_name.send_keys(USER_NAME)
    password.send_keys(PASS_WORD)
    sing_in_button.click()
    time.sleep(10)


def find_followers():
    driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")

    followers_link = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'followers'))
    )
    followers_link.click()
    time.sleep(5)

    # followers_list = driver.find_element(By.CLASS_NAME, 'xs84m0k')
    followers_list = driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div')
    time.sleep(5)
    for i in range(10):
        try:
            followers_list.send_keys(Keys.END)
        except:
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_list)
        time.sleep(2)


def follow_accounts():
    pass


log_in()
find_followers()
