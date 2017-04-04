from django.conf.urls import url
from . import views

app_name = 'book_review'

urlpatterns = [
    url(r'^$', views.start, name = 'start'),
    url(r'^add$', views.add, name='add'),
    url(r'^add_book$', views.add_book, name='add_book'),
    url(r'^(?P<book_id>[0-9]+$)', views.review_book, name="review_book"),
    url(r'^submit_review/(?P<book_id>[0-9]+$)', views.submit_review, name="submit_review"),
    url(r'^users/(?P<user_id>[0-9]+$)', views.user, name="user"),
]
