from django.urls import path

from . import views

urlpatterns = [
    path('new_challenge/', views.create_challenge, name='new_challenge'),
    path('list_challenges/', views.list_challenges, name='list_challenges'),
    path(
        'remove_challenge/<int:id>/',
        views.remove_challenge,
        name='remove_challenge',
    ),
    path('challenge/<int:id>/', views.challenge, name='challenge'),
]
