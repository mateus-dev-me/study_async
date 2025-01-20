from django.urls import path

from . import views

app_name = 'challenges'
urlpatterns = [
    path('new_challenge/', views.create_challenge, name='create'),
    path('list_challenges/', views.list_challenges, name='list'),
    path(
        'remove_challenge/<int:id>/',
        views.remove_challenge,
        name='remove',
    ),
    path('challenge/<int:id>/', views.challenge, name='detail'),
]
