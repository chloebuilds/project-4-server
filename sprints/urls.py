from django.urls import path
from .views import SprintView, SprintGoalView, MoodView

urlpatterns = [
    path('', SprintView.as_view()),
    path('<int:sprint_pk>/sprint_goals/', SprintGoalView.as_view()),
    path('<int:sprint_pk>/moods/', MoodView.as_view()),
]