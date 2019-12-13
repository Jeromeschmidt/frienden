from django.test import TestCase, Client
from django.contrib.auth.models import User
from roommate_finder.models import Person
from roommate_finder.views import PersonDetailView

# Create your tests here.
class RoommateFinderTestCase(TestCase):
    def test_true_is_true(self):
        """ Tests if True is equal to True. Should always pass. """
        self.assertEqual(True, True)

    def test_page_slugify_on_save(self):
            """ Tests the slug generated when saving a Page. """
            # Author is a required field in our model.
            # Create a user for this test and save it to the test database.
            user = User()
            user.save()

            # Create and save a new page to the test database.
            person = Person(first_name = "test person", last_name = "test person", Bio = "test person", Have_room_available = True, min_rent = 1000, max_rent = 2000, contact_info ="test person", pub_date ="2019-12-08T15:48:26-08:00")
            person.save()

            # Make sure the slug that was generated in Page.save()
            # matches what we think it should be.
            self.assertEqual(person.slug, "test-person")

class PersonListViewTests(TestCase):

    def test_multiple_pages(self):
        # Make some test data to be displayed on the page.
        user = User.objects.create()

        person1 = Person(first_name = "test person1", last_name = "test person1", Bio = "test person1", Have_room_available = True, min_rent = 1000, max_rent = 2000, contact_info ="test person", pub_date ="2019-12-08T15:48:26-08:00")
        person2 = Person(first_name = "test person2", last_name = "test person2", Bio = "test person2", Have_room_available = True, min_rent = 1000, max_rent = 2000, contact_info ="test person", pub_date ="2019-12-08T15:48:26-08:00")
        person1.save()
        person2.save()
        # Issue a GET request to the MakeWiki homepage.
        # When we make a request, we get a response back.
        response = self.client.get('/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the number of pages passed to the template
        # matches the number of pages we have in the database.
        responses = response.context['people']
        self.assertEqual(len(responses), 2)

        self.assertQuerysetEqual(
            responses,
            ['<Person: test person1>', '<Person: test person2>'],
            ordered=False
        )

    def test_single_page(self):
        # Issue a GET request to the MakeWiki homepage.
        # When we make a request, we get a response back.
        user = User.objects.create()

        person1 = Person(first_name = "test person1", last_name = "test person1", Bio = "test person1", Have_room_available = True, min_rent = 1000, max_rent = 2000, contact_info ="test person", pub_date ="2019-12-08T15:48:26-08:00")
        person1.save()

        response = self.client.get('/test-person1/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the number of pages passed to the template
        # matches the number of pages we have in the database.
        responses = response.context['person']

        self.assertEqual(str(responses), "test person1")


    def test_view_form_page(self):
        response = self.client.get('/new/')
        # Check request succeeded
        self.assertEqual(response.status_code, 200)
        # Check content
        self.assertIn(b'Frienden', response.content)
