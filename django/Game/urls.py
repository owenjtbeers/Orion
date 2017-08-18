from django.conf.urls import url
from django.views import View

from Game import views

urlpatterns = [
	url(r'^$', views.GameView.as_view()),
]