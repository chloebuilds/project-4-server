from django.urls import path
from .views import SprintListView, SprintDetailView 
from .views import SprintHabitListView, SprintHabitDetailView, SprintGoalListView, SprintGoalDetailView
from .views import DailyMoodListView, DailyMoodDetailView, DailyToDoListView, DailyToDoDetailView
from .views import DailyEnergyListView, DailyEnergyDetailView, DailyGratitudeListView, DailyGratitudeDetailView
from .views import WeeklyIntentionListView, WeeklyIntentionDetailView


urlpatterns = [
    path('', SprintListView.as_view()),
    path('<int:pk>/', SprintDetailView.as_view()),

    path('<int:sprint_pk>/sprint-goals/', SprintGoalListView.as_view()),
    path('<int:sprint_pk>/sprint-goals/<int:sprint_goal_pk>/', SprintGoalDetailView.as_view()),

    path('<int:sprint_pk>/sprint-habits/', SprintHabitListView.as_view()),
    path('<int:sprint_pk>/sprint-habits/<int:sprint_habit_pk>/', SprintHabitDetailView.as_view()),

    path('<int:sprint_pk>/moods/', DailyMoodListView.as_view()),
    path('<int:sprint_pk>/moods/<int:mood_pk>/', DailyMoodDetailView.as_view()),

    path('<int:sprint_pk>/to-dos/', DailyToDoListView.as_view()),
    path('<int:sprint_pk>/to-dos/<int:to_do_pk>/', DailyToDoDetailView.as_view()),

    path('<int:sprint_pk>/energy-levels/', DailyEnergyListView.as_view()),
    path('<int:sprint_pk>/energy-levels/<int:energy_level_pk>/', DailyEnergyDetailView.as_view()),

    path('<int:sprint_pk>/gratitudes/', DailyGratitudeListView.as_view()),
    path('<int:sprint_pk>/gratitudes/<int:gratitude_pk>/', DailyGratitudeDetailView.as_view()),

    path('<int:sprint_pk>/intentions/', WeeklyIntentionListView.as_view()), 
    path('<int:sprint_pk>/intentions/<int:intention_pk>/', WeeklyIntentionDetailView.as_view()), 
]
