from django.urls import path
from . import views
urlpatterns = [        
    path('principal/', views.principalPage, name='principal'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
    path('changePassword',views.changePassword,name='changePassword'),
]
