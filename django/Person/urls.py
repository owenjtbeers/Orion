from django.conf.urls import url
from django.views import View

from Person import views

urlpatterns = [
	url(r'^$', views.PersonView.as_view()),
	url(r'Player/', views.PlayerView.as_view())
]