from django.conf.urls import url
from django.contrib import admin
from posts.views import post_create, post_detail, post_list, post_update, post_delete

urlpatterns = [
    url(r'^list/$', post_list, name='post_list'),
    url(r'^create/$', post_create, name='post_create'),
    url(r'^detail/$', post_detail, name='post_detail'),
    url(r'^update/$', post_update, name='post_update'),
    url(r'^delete/$', post_delete, name='post_delete'),
]