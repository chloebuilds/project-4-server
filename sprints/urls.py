from django.urls import path
from .views import EnergyView, SprintView,  MoodView, DailyToDoListView, DailyToDoDetailView, GratitudeView
from .views import SprintGoalView, SprintHabitView, SprintDetailView, IntentionView, SprintHabitView


urlpatterns = [
    path('', SprintView.as_view()),
    path('<int:pk>/', SprintDetailView.as_view()),

    path('<int:sprint_pk>/sprint-goals/', SprintGoalView.as_view()),
 

    path('<int:sprint_pk>/sprint-habits/', SprintHabitView.as_view()),

    path('<int:sprint_pk>/moods/', MoodView.as_view()),

    path('<int:sprint_pk>/daily-to-dos/', DailyToDoListView.as_view()),
    path('<int:sprint_pk>/daily-to-dos/<int:to_do_pk>', DailyToDoDetailView.as_view()),

    path('<int:sprint_pk>/energies/', EnergyView.as_view()),

    path('<int:sprint_pk>/daily-gratitudes/', GratitudeView.as_view()),

    path('<int:sprint_pk>/weekly-intentions/', IntentionView.as_view()), 
]
