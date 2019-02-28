import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


EXECUTABLE_PATH ='/mnt/c/workspace/django-tdd/install/chromedriver.exe'
LOCAL_HOST_URL = ' http://127.0.0.1:8000/'

start = time.time()
chrome_options = Options()
chrome_options.add_argument("--disable-infobars")

driver = webdriver.Chrome(
  executable_path = EXECUTABLE_PATH,
  chrome_options=chrome_options,
)
driver.get(LOCAL_HOST_URL)

assert 'Django' in driver.title

end = time.time()
print("process {0} ms".format((end - start) * 1000))
sys.exit()

driver.quit()
