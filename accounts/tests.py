from django.test import TestCase, Client
from django.contrib.auth.models import User


# Create your tests here.
class AccountsTestCase(TestCase):
    def test_true_is_true(self):
        """ Tests if True is equal to True. Should always pass. """
        self.assertEqual(True, True)

    def account_created_on_save(self):
            """ Tests the slug generated when saving a Page. """
            # Author is a required field in our model.
            # Create a user for this test and save it to the test database.
            user = User()
            user.save()

            # Create and save a new page to the test database.
            self.user = User.objects.create_user(username='test', password='0987654321')
            test_user = User.objects.get(username='test')

            # Make sure the slug that was generated in Page.save()
            # matches what we think it should be.
            self.assertEqual(test_user.username, 'test')

    def account_login(self):
            """ Tests the slug generated when saving a Page. """
            # Author is a required field in our model.
            # Create a user for this test and save it to the test database.
            user = User()
            user.save()

            # Create and save a new page to the test database.
            self.user = User.objects.create_user(username='test', password='0987654321')
            login = self.client.login(username='test', password='0987654321')

            # Make sure the slug that was generated in Page.save()
            # matches what we think it should be.
            self.assertEqual(login, "test-person")
