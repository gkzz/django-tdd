import os
#from django.test import LiveServerTestCase 
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time


MAX_WAIT = 10

EXECUTABLE_PATH ='/mnt/c/workspace/django-tdd/install/chromedriver.exe'

chrome_options = Options()
chrome_options.add_argument("--disable-infobars")

#class NewVisitorTest(LiveServerTestCase):
class NewVisitorTest(StaticLiveServerTestCase):


    def setUp(self):
        self.driver = webdriver.Chrome(
          executable_path = EXECUTABLE_PATH,
          chrome_options=chrome_options,
        )
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server

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
    
    def test_multiple_users_can_start_lists_at_different_urls(self):
        try:
            self.driver.get(self.live_server_url)
            inputbox = self.driver.find_element_by_id('id_new_item')
            inputbox.send_keys('Buy peacock feathers')
            inputbox.send_keys(Keys.ENTER)
            self.wait_for_row_in_list_table('1: Buy peacock feathers')


            edith_list_url = self.driver.current_url
            self.assertRegex(edith_list_url, '/lists/.+')

            self.driver.quit()
        except:
            self.fail('Failed.')

        try:
            self.driver = webdriver.Chrome(
                executable_path = EXECUTABLE_PATH,
                chrome_options=chrome_options,
            )

            self.driver.get(self.live_server_url)
            page_text = self.driver.find_element_by_tag_name('body').text
            self.assertNotIn('Buy peacock feathers', page_text)
            self.assertNotIn('make a fly', page_text)
   
            inputbox = self.driver.find_element_by_id('id_new_item')
            inputbox.send_keys('Buy milk')
            inputbox.send_keys(Keys.ENTER)
            self.wait_for_row_in_list_table('1: Buy milk')


            francis_list_url = self.driver.current_url
            self.assertRegex(francis_list_url, '/lists/.+')
            self.assertNotEqual(francis_list_url, edith_list_url)


            page_text = self.driver.find_element_by_tag_name('body').text
            self.assertNotIn('Buy peacock feathers', page_text)
            self.assertIn('Buy milk', page_text)
        except:
            self.fail('Failed.')
    
    def test_layout_and_styling(self):
        self.driver.get(self.live_server_url)
        self.driver.set_window_size(1024, 768)


        inputbox = self.driver.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )

        inputbox.send_keys('testing')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: testing')
        inputbox = self.driver.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )