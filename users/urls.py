from django.urls import path
from . import views
from django.contrib.auth import views as v

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', v.LoginView.as_view(), name='login'),
    path('logout/', v.LogoutView.as_view(), name='logout'),
    path('profile/', views.edit_profile, name='edit_profile'),

    path('password_reset/', v.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done', v.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', v.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done', v.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('delete_from_cart/<int:product_id>/', views.delete_from_cart, name='delete_from_cart')
]