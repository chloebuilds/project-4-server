from django.contrib import admin
from .models import Sprint, SprintGoal, Mood

admin.site.register(Sprint)
admin.site.register(SprintGoal)
admin.site.register(Mood)