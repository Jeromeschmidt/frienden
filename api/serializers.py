from rest_framework.serializers import ModelSerializer

from roommate_finder.models import Person

class PersonSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

# class ChoiceSerializer(ModelSerializer):
#     class Meta:
#         model = Choice
#         fields = '__all__'
