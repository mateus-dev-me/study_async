from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('create/', views.create, name='create'),
    path('login/', views.signin, name='login'),
    path('logout/', views.logout, name='logout'),
]
