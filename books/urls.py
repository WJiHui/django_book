from django.conf.urls import include, url
from books import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^search/$', views.search),
    url(r'^(?P<title>\w+)/page(?P<num>\w+)/', views.book),
]
