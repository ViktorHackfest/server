from django.urls import path
from .views import MyUserDetailView

urlpatterns = [
    path('login', MyUserDetailView.as_view()),
]