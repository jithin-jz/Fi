from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('', views.signup_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
