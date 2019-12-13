from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.forms import ModelForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User

from roommate_finder.models import Person
from roommate_finder.forms import PersonForm


class PersonListView(ListView):
    """ Renders a list of all Pages. """
    model = Person

    def get(self, request):
        """ GET a list of Pages. """
        # min_rent = Person.objects.get(model.first_name = request.user.username)
        # print(min_rent)
        # max_rent = None
        people = self.get_queryset().all().order_by('-pub_date')
        return render(request, 'list.html', {
          'people': people
        })

class PersonDetailView(DetailView):
    """ Renders a specific page based on it's slug."""
    model = Person

    def get(self, request, slug):
        """ Returns a specific wiki page by slug. """
        person = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'person.html', {
          'person': person
        })

class PersonCreate(CreateView):
    model = Person
    fields = ['first_name', 'last_name', 'Bio', 'Have_room_available', 'min_rent', 'max_rent', 'contact_info', 'pub_date']
    template_name = 'new_person.html'
