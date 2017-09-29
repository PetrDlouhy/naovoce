from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^subscribe/(?P<user_pk>\d+)/$', views.subscribtion, name='subscribe'),
    url(r'^unsubscribe/(?P<user_pk>\d+)/$', views.subscribtion, name='unsubscribe'),
]
