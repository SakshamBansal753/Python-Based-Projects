
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_option=webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_option)
driver.get("https://secure-retreat-92358.herokuapp.com/")
Fname=driver.find_element(By.NAME,value="fName")
Fname.send_keys("Saksham")
Lname=driver.find_element(By.NAME,value="lName")
Lname.send_keys("bansal")
em=driver.find_element(By.NAME,value="email")
em.send_keys("bansal@gmail.com",Keys.ENTER)




