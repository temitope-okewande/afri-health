import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#get the driver
servix_obj= Service("C:\Driver\edgedriver_win64\msedgedriver.exe")
driver=webdriver.Chrome(service=servix_obj)
#mmaximize window
driver.maximize_window()
#open browser
driver.get("https://testing-doctor.rigourplus.com/")
driver.find_element(By.XPATH, '//a[contains(@href,"/sign-in")]').click()
driver.find_element(By.NAME, "email").send_keys("topehnics+Polaris080@gmail.com")
driver.find_element(By.NAME, "password").send_keys("@Test123")
time.sleep(0.2)
driver.find_element(By.CLASS_NAME, "sc-d37aa103-0").click()
time.sleep(0.5)