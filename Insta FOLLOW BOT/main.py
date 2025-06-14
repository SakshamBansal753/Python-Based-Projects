SIMILIAR_ACCOUNT="ACC YOU WANT TOFOLLOW"
USER_NAME="Your USErname"
USER_PASS="PAsS"
from selenium import  webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import  time
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)

driver.get("https://www.instagram.com/")
wait=WebDriverWait(driver,15)
user_field=wait.until(EC.presence_of_element_located((By.NAME,"username")))
user_field.send_keys(USER_NAME)
pass_field=wait.until(EC.presence_of_element_located((By.NAME,"password")))
pass_field.send_keys(USER_PASS,Keys.ENTER)

try:
    not_now_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@role='button' and text()='Not now']"))
    )
    not_now_btn.click()
except Exception as e:
    print("Failed to find 'Not now' button:", e)

searchs=WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'Search'))
    )
searchs.click()
enter=WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div/input'))
    )
enter.send_keys(SIMILIAR_ACCOUNT)

Account=WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/a[1]'))
)
Account.click()

Follow=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[2]/div/div/div[2]/div/div[1]/button'))
)
Follow.click()
