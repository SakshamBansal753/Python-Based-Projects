import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
PROMISED_DOWN = 150
PROMISED_UP = 10
YOUR_X_Email="YOur_mail"
Your_X_Pass="Your Pass"

class Speed:
    def __init__(self):
        self.chrome_options=webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach",True)
        self.driver=webdriver.Chrome(options=self.chrome_options)
        self.up=0
        self.down=0
    def get_speed(self):
        time.sleep(3)
        self.driver.get("https://www.speedtest.net/")
        self.go=self.driver.find_element(By.CSS_SELECTOR,value='#container > div.pre-fold > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-view > div > div.start-button > a')
        self.go.click()
        time.sleep(60)
        self.up=self.driver.find_element(By.XPATH,value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        print(self.up.text)
        self.down=self.driver.find_element(By.XPATH,value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]')
        print(self.down.text)
    def tweet(self):

        self.driver.get("https://x.com/home")
        wait = WebDriverWait(self.driver, 15)

        email_field = wait.until(EC.presence_of_element_located((By.NAME, "text")))
        email_field.send_keys(YOUR_X_Email,Keys.ENTER)
        time.sleep(3)
        use_field=wait.until(EC.presence_of_element_located((By.NAME,"text")))
        use_field.send_keys("Your User name",Keys.ENTER)
        time.sleep(2)
        pass_field=wait.until(EC.presence_of_element_located((By.NAME,"password")))
        pass_field.send_keys(Your_X_Pass,Keys.ENTER)
        time.sleep(5)
        # Step 2: Wait for homepage and tweet box
        tweet_box = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="placeholder-8onjp"]')
        ))
        tweet_box.click()
        tweet_box.send_keys("Your X")



bot=Speed()
bot.get_speed()
bot.tweet()

