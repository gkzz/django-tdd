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
from selenium.common.exceptions import WebDriverException
import time

MAX_WAIT = 10

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

    
    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.driver.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr') 
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_for_one_user(self):
        try:
            self.driver.get(self.live_server_url)
            
            self.assertIn('Django-tdd', self.driver.title)
            header_text = self.driver.find_element_by_tag_name('h1').text
            self.assertIn('To-Do list',header_text)

            # She is invited to enter a to-do item straight away
            inputbox = self.driver.find_element_by_id('id_new_item')
            self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
            )

            # She types "Buy peacock feathers" into a text box (Edith's hobby
            # is tying fly-fishing lures)
            inputbox.send_keys('Buy peacock feathers')


            # When she hits enter, the page updates, and now the page lists
            # "1: Buy peacock feathers" as an item in a to-do list table
            inputbox.send_keys(Keys.ENTER)
            self.wait_for_row_in_list_table('1: Buy peacock feathers')

            inputbox = self.driver.find_element_by_id('id_new_item')
            inputbox.send_keys('Use peacock feathers to make a fly')
            inputbox.send_keys(Keys.ENTER)

            self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')
            self.wait_for_row_in_list_table('1: Buy peacock feathers')

            #self.fail('Finished, and successful!')
        except:
            self.fail('Failed.')


