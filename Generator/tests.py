from django.test import SimpleTestCase
from django.urls import reverse, resolve
from Generator.views import index, signup, cronjob, execute_cronjobs, test01, test02, test03, testing


class TestUrls(SimpleTestCase):

    def test_index(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, index)

    def test_signup(self):
        url = reverse('signup')
        self.assertEqual(resolve(url).func, signup)

    def test_cronjob(self):
        url = reverse('CreateCronJob')
        self.assertEqual(resolve(url).func, cronjob)

    def test_execute_cronjobs(self):
        url = reverse('ExecuteCronJobs')
        self.assertEqual(resolve(url).func, execute_cronjobs)

    def test_test01(self):
        url = reverse('Test01')
        self.assertEqual(resolve(url).func, test01)

    def test_test02(self):
        url = reverse('Test02')
        self.assertEqual(resolve(url).func, test02)

    def test_test03(self):
        url = reverse('Test03')
        self.assertEqual(resolve(url).func, test03)

    def test_testing(self):
        url = reverse('testing')
        self.assertEqual(resolve(url).func, testing)
