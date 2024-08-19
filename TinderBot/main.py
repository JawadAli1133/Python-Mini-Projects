import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(chrome_options)

time.sleep(3)
driver.get('https://tinder.com/')

sing_in = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="o131391810"]/div/div[1]'
                                        '/div/main/div[1]/div/div/div/div/div/'
                                        'header/div/div[2]/div[2]/a/div[2]/div[2]/div'))
)
sing_in.click()

continue_with_facebook = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="o-1596989266"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div[2]/div/div'))
)
continue_with_facebook.click()

WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

phone_number = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="email"]'))
)
password = driver.find_element(By.XPATH, value='//*[@id="pass"]')
phone_number.send_keys('03414654664')
password.send_keys('jawadddd')

sing_in_button = driver.find_element(By.ID, value='loginbutton')
sing_in_button.click()

time.sleep(10)
driver.close()

driver.switch_to.window(base_window)
continue_with_facebook.click()

allow_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="o-1596989266"]/div/div/div/div/div[3]/button[1]/div[2]/div[2]'))
)
allow_button.click()

i_accept_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="o-1596989266"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]/div'))
)
i_accept_button.click()

miss_out_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'lxn9zzn'))
)
miss_out_button.click()
while True:
    time.sleep(5)
    nope_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.CLASS_NAME, '//*[@id="o131391810"]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div[1]/div/div[3]/div/div[2]/button'))
    )
    nope_button.click()

