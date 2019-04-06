# soruces;
# How do you test that a Python function throws an exception?
# https://stackoverflow.com/questions/129507/how-do-you-test-that-a-python-function-throws-an-exception?rq=1

"""
import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import unittest
"""

from django.test import LiveServerTestCase 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys 
import time



#class NewVisitorTest(unittest.TestCase):
class NewVisitorTest(LiveServerTestCase):

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

    
    def check_for_row_in_list_table(self, row_text):
        try:
            table = self.browser.find_element_by_id('id_list_table') 
            rows = table.find_elements_by_tag_name('tr') 
            self.assertIn(row_text, [row.text for row in rows])
        except:
            self.fail('fail the test')


    def test_can_start_a_list_and_retrieve_it_later(self):
        self.driver.get(self.live_server_url)



if __name__ == '__main__':
    unittest.main(warnings='ignore')
