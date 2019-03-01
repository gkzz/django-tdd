# soruces;
# How do you test that a Python function throws an exception?
# https://stackoverflow.com/questions/129507/how-do-you-test-that-a-python-function-throws-an-exception?rq=1


import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        EXECUTABLE_PATH ='/mnt/c/workspace/django-tdd/install/chromedriver.exe'

        chrome_options = Options()
        chrome_options.add_argument("--disable-infobars")
        self.driver = webdriver.Chrome(
          executable_path = EXECUTABLE_PATH,
          chrome_options=chrome_options,
        )

    def tearDown(self):
        self.driver.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        LOCAL_HOST_URL = 'http://127.0.0.1:8000/'

        self.driver.get(LOCAL_HOST_URL)
        try:
            #self.assertIn('To-Do', self.driver.title)
            self.assertIn('Django', self.driver.title)
        #except Exception as e:
        except AssertionError as AE:
            self.fail('Unexpected exception raised:', AE)
        else:
            self.fail('ExpectedException not raised')


if __name__ == '__main__':
    unittest.main(warnings='ignore')


