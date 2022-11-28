from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# open web browser

serv_obj = Service("C:/Driver/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()

# open the page url
driver.get("https://testing-doctor.rigourplus.com/")
# Click on sign in button
driver.find_element(By.XPATH, '//a[contains(@href,"/sign-in")]').click()
time.sleep(0.5)
# Enter email address
driver.find_element(By.NAME, "email").send_keys("topehnics+Polaris080@gmail.com")
time.sleep(0.5)
# Enter password
driver.find_element(By.NAME, "password").send_keys("@Test123")
time.sleep(0.5)
# click on Login

time.sleep(5.0)
