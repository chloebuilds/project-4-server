from django.urls import path
from .views import LoginView, RegisterView, ProfileView, ResetView

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("login/", LoginView.as_view()),
    path("profile/<int:pk>/", ProfileView.as_view()),
    path("profile/<int:pk>/reset/", ResetView.as_view())
]