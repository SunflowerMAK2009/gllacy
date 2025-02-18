from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home_url'),
    path('email/', views.email_view, name='email_url'),
    path('popup/', views.popup_view, name='popup'),
    path('thanks/', views.thanks_view, name='thanks_url'),
    path('search/', views.search, name='search')
]

