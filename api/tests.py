from django.test import TestCase, Client
from django.contrib.auth.models import User


# Create your tests here.
class AccountsTestCase(TestCase):
    def test_true_is_true(self):
        """ Tests if True is equal to True. Should always pass. """
        self.assertEqual(True, True)

    def api_is_active(self):
            """ Tests the slug generated when saving a Page. """
            # Author is a required field in our model.
            # Create a user for this test and save it to the test database.
            user = User()
            user.save()

            # Create and save a new page to the test database.
            response = self.client.get('/api/roommate_finder')

            # Make sure the slug that was generated in Page.save()
            # matches what we think it should be.
            self.assertEqual(response, 200)

    def api_can_update(self):
            """Test the api can update a given bucketlist."""
            person1 = Person(first_name = "test person1", last_name = "test person1", Bio = "test person1", Have_room_available = True, min_rent = 1000, max_rent = 2000, contact_info ="test person", pub_date ="2019-12-08T15:48:26-08:00")
            person2 = Person(first_name = "test person2", last_name = "test person2", Bio = "test person2", Have_room_available = True, min_rent = 1000, max_rent = 2000, contact_info ="test person", pub_date ="2019-12-08T15:48:26-08:00")
            person1.save()
            person2.save()
            update_person = self.client.put(
                reverse('details', kwargs={'pk': person1.id}),
                person2, format='json'
            )
            self.assertEqual(res.status_code, 200)
