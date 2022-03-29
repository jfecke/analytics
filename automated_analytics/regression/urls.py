from django.conf.urls import url
from regression import views

# TEMPLATE TAGGING
app_name = 'regression'

urlpatterns = [
    url(r'^user/$', views.users, name='user'),
    url(r'^other/$', views.other, name='other'),
    url(r'^relative/$', views.relative_URL, name='relative_URL')
]