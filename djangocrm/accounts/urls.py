from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *


urlpatterns = [
    path('', home,name='home'),
    path('user',users,name='user'),
    path('customer/<str:pk>', customer,name='customer'),
    path('products', product,name='products'),
    path('create_order', create_order,name='create_order'),
    path('update_order/<str:pk>', update_order,name='update_order'),
    path('update_remove/<str:pk>', update_remove,name='update_remove'),
    path('register', register,name='register'),
    path('login', loginPage,name='login'),
    path('logout', logoutPage,name='logout'),
    path('profile', account_setting,name='account_setting'),


    path('reset_password/',
         auth_views.PasswordResetView.as_view(),
         name="reset_password"),

    path('reset_password_sent/',
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),

    path('reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete"),


]