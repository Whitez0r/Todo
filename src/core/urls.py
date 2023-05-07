from django.urls import path
from src.core import views

urlpatterns = [
    path('signup', views.SignupView.as_view(), name='signup'),
]
