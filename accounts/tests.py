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


class ProfileTests(APITestCase):
    def setUp(self): 
#        import ipdb; ipdb.set_trace()
        self.url = reverse('profile-list')
        self.user = User.objects.create_user(
            username='test_user', email='u@d.com', password='password')

    def test_anonymous_profile(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(
            response.data,
            {"detail":"Authentication credentials were not provided."}
        )

    def test_user_profile(self):

        response = self.client.get(self.url, format='json')
        self.client.login(username='test_user', password='password')
        response = self.client.get(self.url, format='json')
        self.assertEqual(
            response.data,
            []
        )

        #response = self.client.get(self.url, format='json')
        self.client.login(username='test_user', password='password')
        data = {'address' : 'number street, city state zip'}
        response = self.client.post(self.url, data, format='json')
        data.update({'owner': 1})
        self.assertEqual(
            response.data,
            data
        )
        response = self.client.get(self.url, format='json')
        self.assertEqual(
            response.data[0],
            data
        )
        def test_user_permissions(self):
            self.test_user_profile()
            malicious_user = User.objects.create_user(
            username='malicious_user', email='u@d.com', password='password')
            url  = os.path.join(self.url,self.user.pk) +'/'
            self.client.login(username='malicious_user', password='password')

            response = self.client.get(self.url, format='json',follow=True)
#            response = self.client.get(self.url, format='json')
            self.assertEqual(
                response.data,
                {"detail": "You do not have permission to perform this action."}
            )

        #"detail": "You do not have permission to perform this action."


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
        
    def test_user_login(self):
        driver = self.driver
        driver.get(urllib.parse.urljoin(self.live_server_url,'home'))

class AccountTests(APITestCase):
    def test_profile(self):
        pass
#    def test_create_admin_account(self):
#        pass


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



