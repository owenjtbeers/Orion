from django.conf.urls import url
from django.views import View

from League import views

urlpatterns = [
	url(r'^$', views.LeagueView.as_view()),
]