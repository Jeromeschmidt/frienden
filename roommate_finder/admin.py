from django.contrib import admin
from roommate_finder.models import Person


class PersonAdmin(admin.ModelAdmin):
    """ Show helpful fields on the changelist page. """
    list_display = ('first_name', 'last_name', 'Bio', 'Have_room_available', 'min_rent', 'max_rent', 'pub_date')

admin.site.register(Person, PersonAdmin)
