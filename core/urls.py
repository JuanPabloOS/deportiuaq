from django.urls import path
from . import views
urlpatterns = [    
    path('principal/',views.principalPage, name='principal'),
    path('login/', views.login, name='login'),
]
