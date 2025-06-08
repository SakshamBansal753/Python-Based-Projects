from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
chrome_option=webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_option)
driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie=driver.find_element(By.ID,value="cookie")
items=driver.find_elements(By.CSS_SELECTOR,value="#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout=time.time()+5
fivemin=time.time()+60*5

while True:
    cookie.click()
    if time.time()>timeout:
        all_prices=driver.find_elements(By.CSS_SELECTOR,value="#store b")
        item_price=[]
        for price in all_prices:
            element=price.text
            if "-" in element:
                cost = int(element.split("-")[1].strip().replace(",", ""))
                item_price.append(cost)

        cookie_upgrade={}
        for n in range(len(item_price)):
            cookie_upgrade[item_price[n]] = item_ids[n]

        money_element=driver.find_element(By.ID,value="money").text
        if "," in money_element:
            money_element=money_element.replace(",","")
        cookies=int(money_element)
        affordable={}
        for cost,id in cookie_upgrade.items():
            if cookies>cost:
                affordable[cost]=id
        highest=max(affordable)
        to_id=affordable[highest]

        driver.find_element(By.ID,value=to_id).click()
        timeout=time.time()+5

    if time.time() > fivemin:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        break
