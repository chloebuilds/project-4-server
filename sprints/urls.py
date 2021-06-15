from django.urls import path
from .views import SprintView, SprintGoalView, MoodView, DailyToDoListView, EnergyView, IntentionView, SprintDetailView

urlpatterns = [
    path('', SprintView.as_view()),
    path('<int:pk>/', SprintDetailView.as_view()),
    path('<int:sprint_pk>/sprint-goals/', SprintGoalView.as_view()),
    path('<int:sprint_pk>/moods/', MoodView.as_view()),
    path('<int:sprint_pk>/energy-level/', EnergyView.as_view()),
    path('<int:sprint_pk>/daily-todo/', DailyToDoListView.as_view()),
    path('<int:sprint_pk>/daily-gratitude/', DailyToDoListView.as_view()),
    path('<int:sprint_pk>/weekly-intention/', IntentionView.as_view()),
]
