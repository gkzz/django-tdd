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
           
        try:
            self.assertTrue( html.startswith('<!DOCTYPE html>'))
            #self.assertEqual('<title>Django-tdd</title>', html)
        except:
            self.fail('Finish the test!')
    

    def test_home_page_returns_correct_html_for_loop(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')

        test_args_list = [
            # self.assertIn(X, Y) check "Y in X"
            ("<!DOCTYPE html>", html),  
            #("<html><title>Error", html),
            ("<title>Django-tdd", html),
            #("<html><title>Django-tdd</title></html>", html),
            #("<html><title>Django-tdd</title></html><body><h1>This is error!</h1></body>", html),
        ]
        
        for x,  y in test_args_list:
            with self.subTest(x=x, y=y):
                self.assertIn(x, y)
            
        