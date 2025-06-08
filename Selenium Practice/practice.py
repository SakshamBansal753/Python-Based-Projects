from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_option=webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_option)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
stats=driver.find_element(By.CSS_SELECTOR,value="#articlecount  ul  li:nth-child(2)  a:nth-child(1) ")
all_portals=driver.find_element(By.LINK_TEXT,value="Content portals")
#all_portals.click()
#find Search
search=driver.find_element(By.NAME,value="search")
#sending input to search
search.send_keys("Python",Keys.ENTER)


