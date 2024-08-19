from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(chrome_options)

driver.get('https://www.leetcode.com')

sing_in_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="landing-page-app"]/div/div[1]/div[3]/div[1]/div/div/div[2]/div/a[5]'))
)

sing_in_button.click()

email = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="id_login"]'))
)
password = driver.find_element(By.XPATH, '//*[@id="id_password"]')
email.send_keys('jawadaliamjad1113@gmail.com')
password.send_keys('Jawad_ali1133')
sing_in = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="signin_btn"]'))
)
sing_in.click()

time.sleep(10)
contest_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="leetcode-navbar"]/div[1]/ul/li[3]/a'))
)
contest_button.click()
weekly_contest = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[1]/div[4]/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/a/div[2]/div/div[1]/div/span'))
)
weekly_contest.click()

register_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="contest-app"]/div/div/div[3]/span/a'))
)
register_button.click()

sure_register = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div/div[10]/button[1]'))
)
sure_register.click()


