from django.urls import path
from . import views

urlpatterns=[
    path('', views.index , name='index' ),
    path('search', views.search, name='search'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('user', views.user, name='user'),
    path('cazare/<str:pk>', views.cazare, name='cazare'),
    path('new', views.new, name='new'),
    path('main', views.main, name='main')
]