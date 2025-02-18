#dwld webdriver nd pass as parameter
# selenium/Scripts/activate
#pip install selenium
#built in linux machine(headless mode)-hw
#without ui how its working
#run selenium testcases(headless selenium)
#when ever there is failure...error msg


from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
time.sleep(10)
driver.close()
print("test  passed")