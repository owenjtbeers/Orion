from django.conf.urls import url
from django.views import View 

from Team import views

urlpatterns = [
	url(r'^$', views.TeamView.as_view()),
	url(r'Roster/names', views.RosterNamesView.as_view())
]