from django.conf.urls import url, include
from . import views

app_name = 'login_registration'

urlpatterns = [
    url(r'^$', views.start, name='start'),
    url(r'^actions', views.submit, name='actions'),
]
