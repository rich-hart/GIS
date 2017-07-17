from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User, Group


from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
#from myproject.apps.core.models import Account
from selenium import webdriver
from django.test import LiveServerTestCase
import shutil
import os
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import urllib


from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory

#class LoginTest(TestCase):
#    def setUp(self):
#        self.factory = RequestFactory()
#        self.admin_user = User.objects.create_superuser(
#            'admin',
#            'u@d.com',
#            'password123',
#        )
#
#        self.user = User.objects.create_user(
#            username='jacob', email='jacob@…', password='top_secret')
#    def test_admin(self):
      
class TestLiveLogin(LiveServerTestCase):
    serialized_rollback = True
    def tearDown(self):
        self.driver.quit()
        super(LiveServerTestCase, self).tearDown()

    def setUp(self):
        super(LiveServerTestCase, self).setUp()
        admin_user = User.objects.create_superuser(
            'admin', 
            'u@d.com', 
            'password123',
        )
        admin_user.save()
        if False:
            self.driver = webdriver.Chrome()
        else:

            try:
                phantomjs_path = os.environ['phantomjs']
            except KeyError:
                phantomjs_path = shutil.which("phantomjs")
            self.driver = webdriver.PhantomJS(executable_path=phantomjs_path)

    def test_admin_login(self):
#        import ipdb; ipdb.set_trace()
        driver = self.driver
        driver.get(urllib.parse.urljoin(self.live_server_url,'admin'))
        self.assertIn('/admin/login/?next=/admin/',driver.current_url)
        username_field = driver.find_element_by_id('id_username')
        username_field.send_keys('admin')
        password_field = driver.find_element_by_id('id_password')
        password_field.send_keys('password123')
        login_button  = driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input'
)       
        login_button.click()
        self.assertEqual(
            driver.current_url,
            urllib.parse.urljoin(self.live_server_url,'admin/')
        )
        self.assertIn(
            'Welcome',
            driver.page_source
        )        
#        login_button = driver.find_element_by_tag_name('input')
#        login_button.click()
#        self.assertEqual(
#            driver.current_url, 
#            'http://localhost:8001/admin/login/?next=/admin/'
#        )
#        username_field = driver.find_element_by_name("auth_key")
#        username_field.send_keys('admin')
#        password_field = driver.find_element_by_name("password")
#        password_field.send_keys('password123')
#        sign_in_button = driver.find_element_by_class_name("standard")
#        sign_in_button.click()
        


class AccountTests(APITestCase):
    def test_create_admin_account(self):
        pass


#        """
#        Ensure we can create a new account object.
#        """
#        url = reverse('account-list')
#        data = {'name': 'DabApps'}
#        response = self.client.post(url, data, format='json')
#        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#        self.assertEqual(Account.objects.count(), 1)
#        self.assertEqual(Account.objects.get().name, 'DabApps')



class AccountTestCase(TestCase):

    def setUp(self):
        
        self.client = Client()

    def test_admin(self):
        admin = User.objects.create_user(
            'admin', 
            'admin@test.com', 
            'pass'
        )
        admin.save()
#        response =self.client.post(
#            '/admin/',
#            {
#                'username': 'john', 
#                'password': 'smith'
#            }
#        , follow=True)
#        self.assertEqual(response.status_code,400)

    def test_staff(self):
        pass

    def test_anonymous(self):
        pass

    def test_user(self):
        pass

    def test_contact_information(self):
        pass
    
class TestOAuth2(TestCase):
    def test_facebook(self):
        pass



