from django.conf.urls import url
from regression import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]