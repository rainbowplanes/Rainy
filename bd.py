import time
from selenium import webdriver
 
driver = webdriver.Chrome()

driver.get("https://www.baidu.com/")

driver.find_element_by_id("kw").send_keys("python")

driver.find_element_by_id('su').click()

time.sleep(3)

driver.quit()
