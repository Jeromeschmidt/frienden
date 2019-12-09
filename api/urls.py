from django.urls import path

from api.views import PersonList, PersonDetail

urlpatterns = [
    path('roommate_finder/', PersonList.as_view(), name='person_list'),
    # path('wiki/<computer-science>', PageDetail.as_view(), name='page_detail')
]
