from django.urls import path
from .views import SprintView, SprintGoalView, MoodView, EnergyView

urlpatterns = [
    path('', SprintView.as_view()),

    path('<int:sprint_pk>/sprint-goals/', SprintGoalView.as_view()),

    path('<int:sprint_pk>/moods/', MoodView.as_view()),

    path('<int:sprint_pk>/energy-levels/', EnergyView.as_view()),

]
