from django.urls import path

from api.views import PersonList, PersonDetail

urlpatterns = [
    path('roommate_finder/', PersonList.as_view(), name='person_list'),
    path('roommate_finder/<int:pk>', PersonDetail.as_view(), name='person_detail')
]
