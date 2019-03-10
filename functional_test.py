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
        LOCAL_HOST_URL = 'http://127.0.0.1:8000/'

        self.driver.get(LOCAL_HOST_URL)
        try:
            #self.assertIn('To-Do', self.driver.title)
            self.assertIn('Django', self.driver.title)
            header_text = self.driver.find_element_by_tag_name('h1').text
            self.assertIn('To-Do', header_text)
            inputbox = self.driver.find_element_by_id('id_new_item')
            self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
            )
            inputbox.send_keys('Buy peacock feathers')

            # When she hits enter, the page updates, and now the page lists
            # "1: Buy peacock feathers" as an item in a to-do list table
            inputbox.send_keys(Keys.ENTER)
            time.sleep(1)
            table = self.driver.find_element_by_id('id_list_table')
            rows = table.find_elements_by_tag_name('tr')
            self.assertTrue(
                any(row.text == '1: Buy peacock feathers' for row in rows),
                "New to-do item did not appear in table"
            )
        except:
            self.fail('fail the test')
        
        


if __name__ == '__main__':
    unittest.main(warnings='ignore')
