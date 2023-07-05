from django.urls import path, include 
from . import views

app_name = 'membership' 
urlpatterns = [
    path('member_login/', views.member_login, name='member_login'),
    path('authenticate/', views.authenticate_member, name='authenticate'),
    path('register/', views.register, name='register'),
    path('registration/', views.registration, name='registration'),
    path('overview/', views.overview, name='overview'),
    path('logged_out/', views.logout_member, name='logout_member'),
]