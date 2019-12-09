from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from roommate_finder.models import Person
from api.serializers import PersonSerializer
# from api.serializers import ChoiceSerializer

class PersonList(APIView):
    def get(self, request):
        people = Person.objects.all()[:20]
        data = PersonSerializer(people, many=True).data
        return Response(data)

class PersonDetail(APIView):
    def get(self, request, pk):
        person = get_object_or_404(Person, pk=pk)
        data = PersonSerializer(person).data
        return Response(data)
