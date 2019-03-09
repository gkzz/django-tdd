from django.urls import resolve 
from django.test import TestCase 
from django.http import HttpRequest 
from lists.views import home_page


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
    
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')

        # Tutorial's code is bellow;
        
#        self.assertTrue(html.startswith('<html>'))
#        self.assertTrue(html.endswith('</html>'))
#        self.assertIn('<title>To-Do lists</ title >',html)
#        self.assertTrue(html.endswith('test'))
      

        
        try:
            self.assertTrue( html.startswith('<html>'))
            self.assertIn('<title>Django-tdd</title>', html)
            self.assertEqual('<html><title>Django-tdd</title></html>', html)
        except:
            self.fail('Finish the test!')