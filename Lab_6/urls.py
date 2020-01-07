from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from user import views
from user.views import EventView, UserView, index

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^events/', EventView.as_view()),
    url(r'^users/', UserView.as_view()),
    url(r'^registration/', views.registration, name='registration'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    path('', index),
]
