from django.urls import path
from . import views

urlpatterns = [
    path('longin/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]