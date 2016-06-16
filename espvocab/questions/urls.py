from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.quiz_render, name='quiz_render'),
]