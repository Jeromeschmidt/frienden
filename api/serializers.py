from rest_framework.serializers import ModelSerializer

from roommate_finder.models import Person

class PersonSerializer(ModelSerializer):
    class Meta:
        model = Person

        fields = ('last_name', 'Bio', 'Have_room_available', 'min_rent', 'max_rent', 'pub_date')
