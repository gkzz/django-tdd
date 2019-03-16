# soruces;
# How do you test that a Python function throws an exception?
# https://stackoverflow.com/questions/129507/how-do-you-test-that-a-python-function-throws-an-exception?rq=1


import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
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
        LOCAL_HOST_URL = 'http://127.0.0.1:8000'

        self.driver.get(LOCAL_HOST_URL)
        try:
            #self.assertIn('To-Do', self.driver.title)
            self.assertIn('Django-tdd', self.driver.title)
            header_text = self.driver.find_element_by_tag_name('h1').text
            self.assertIn('To-Do', header_text)

            # She is invited to enter a to-do item straight away
            inputbox = self.driver.find_element_by_id('id_new_item')
            inputbox.send_keys('Use peacock feathers to make a fly')
            inputbox.send_keys(Keys.ENTER)
            time.sleep(1)

            table = self.driver.find_element_by_id('id_list_table')
            rows = table.find_elements_by_tag_name('tr')
            self.assertIn(
                '1: Buy peacock feathers', [row.text for row in rows]
            )
            self.assertIn(
                '2: Use peacock feathers to make a fly', [row.text for row in rows]
            )
        except:
            self.fail('fail the test')
        


if __name__ == '__main__':
    unittest.main(warnings='ignore')
