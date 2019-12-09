from django.forms import ModelForm
from roommate_finder.models import Person


class PersonForm(ModelForm):
    """ Render and process a form based on the Page model. """
    model = Person
