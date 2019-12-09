from django.urls import path
from roommate_finder.views import PersonListView, PersonDetailView, PersonCreate
from accounts.views import SignUpView
from roommate_finder.views import PersonCreate


urlpatterns = [
    path('', PersonListView.as_view(), name='person-list-page'),
    path('new/', PersonCreate.as_view(), name='person-create-page'),
    path('<str:slug>/', PersonDetailView.as_view(), name='person-details-page'),
]
