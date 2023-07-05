from django.urls import path
from . import views

app_name = 'competitions'
urlpatterns = [ 
    path('', views.competition_page, name='competition_page'),
    path('<int:competition_id>/', views.view_competition, name='view_competition'),
    path('<int:competition_id>/enter/', views.enter, name='enter'),    
]