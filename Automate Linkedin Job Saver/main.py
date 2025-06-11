from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
Email="Your_Email"
passes="Your Linkedin Password"
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")
time.sleep(3)
sign_in_btn=driver.find_element(by=By.XPATH,value='//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
sign_in_btn.click()
#signin
time.sleep(3)
email_field=driver.find_element(By.CSS_SELECTOR,value="#base-sign-in-modal_session_key")
email_field.send_keys(Email)
password=driver.find_element(By.CSS_SELECTOR,value="#base-sign-in-modal_session_password")
password.send_keys(passes,Keys.ENTER)
time.sleep(3)
save=driver.find_element(By.XPATH,value='//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div/div[7]/div/button')
save.click()
