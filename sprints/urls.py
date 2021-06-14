from django.urls import path
from .views import SprintView
# , SprintGoalView, MoodView

urlpatterns = [
    path('', SprintView.as_view()),

    # path('<int:sprint_pk>/sprint_goals/', SprintGoalView.as_view()),

    # path('<int:sprint_pk>/moods/', MoodView.as_view()),
    # path("<int:pk>/", DinosaurDetailView.as_view()),
    # # Path for adding a comment to a sprints
    # path("<int:sprints>/comments/", CommentListView.as_view()),
    # # Add an underscore in front of dinosaur_pk because it's not used,
    # # We refer directly to the comment_pk instead and delete that
    # path("<int:_dinosaur_pk>/comments/<int:comment_pk>", CommentListView.as_view()),
]
